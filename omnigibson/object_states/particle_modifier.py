from abc import abstractmethod
from collections import defaultdict
import numpy as np
import omnigibson as og
from omnigibson.macros import create_module_macros, macros, gm
from omnigibson.prims.geom_prim import VisualGeomPrim
from omnigibson.object_states.aabb import AABB
from omnigibson.object_states.contact_bodies import ContactBodies
from omnigibson.object_states.contact_particles import ContactParticles
from omnigibson.object_states.covered import Covered
from omnigibson.object_states.link_based_state_mixin import LinkBasedStateMixin
from omnigibson.object_states.object_state_base import IntrinsicObjectState
from omnigibson.object_states.saturated import ModifiedParticles, Saturated
from omnigibson.object_states.toggle import ToggledOn
from omnigibson.object_states.update_state_mixin import UpdateStateMixin
from omnigibson.systems.system_base import VisualParticleSystem, PhysicalParticleSystem, get_system, \
    is_visual_particle_system, is_physical_particle_system, is_system_active, REGISTERED_SYSTEMS
from omnigibson.utils.constants import ParticleModifyMethod, ParticleModifyCondition, PrimType
from omnigibson.utils.geometry_utils import generate_points_in_volume_checker_function, \
    get_particle_positions_in_frame, get_particle_positions_from_frame
from omnigibson.utils.python_utils import classproperty
from omnigibson.utils.deprecated_utils import Core
from omnigibson.utils.ui_utils import suppress_omni_log
from omnigibson.utils.usd_utils import create_primitive_mesh, FlatcacheAPI
import omnigibson.utils.transform_utils as T
from omnigibson.utils.sampling_utils import sample_cuboid_on_object
from omni.isaac.core.utils.prims import get_prim_at_path, delete_prim, is_prim_path_valid
from pxr import PhysicsSchemaTools, UsdGeom, Gf, Sdf


# Create settings for this module
m = create_module_macros(module_path=__file__)

m.APPLICATION_LINK_PREFIX = "particleapplier"
m.REMOVAL_LINK_PREFIX = "particleremover"

# How many samples within the application area to generate per update step
m.MAX_VISUAL_PARTICLES_APPLIED_PER_STEP = 2
m.MAX_PHYSICAL_PARTICLES_APPLIED_PER_STEP = 10

# How many steps between generating particle samples
m.N_STEPS_PER_APPLICATION = 5
m.N_STEPS_PER_REMOVAL = 1

# Saturation thresholds -- maximum number of particles that can be applied by a ParticleApplier
m.VISUAL_PARTICLES_APPLICATION_LIMIT = 1000000
m.PHYSICAL_PARTICLES_APPLICATION_LIMIT = 1000000

# Saturation thresholds -- maximum number of particles that can be removed ("absorbed") by a ParticleRemover
m.VISUAL_PARTICLES_REMOVAL_LIMIT = 40
m.PHYSICAL_PARTICLES_REMOVAL_LIMIT = 400

# Fallback particle visualization radius for visualizing projected visual particles
m.VISUAL_PARTICLE_PROJECTION_PARTICLE_RADIUS = 0.01

# The margin (> 0) to add to the remover area's AABB when detecting overlaps with other objects
m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN = 0.05

# Settings for determining how the projection particles are visualized as they're projected
m.PROJECTION_VISUALIZATION_CONE_TIP_RADIUS = 0.001
m.PROJECTION_VISUALIZATION_RATE = 200
m.PROJECTION_VISUALIZATION_SPEED = 2.0
m.PROJECTION_VISUALIZATION_ORIENTATION_BIAS = 1e6
m.PROJECTION_VISUALIZATION_SPREAD_FACTOR = 0.8


def create_projection_visualization(
        prim_path,
        shape,
        projection_name,
        projection_radius,
        projection_height,
        particle_radius,
        parent_scale,
        material=None,
):
    """
    Helper function to generate a projection visualization using Omniverse's particle visualization system


    Args:
        prim_path (str): Stage location for where to generate the projection visualization
        shape (str): Shape of the projection to generate. Valid options are: {Sphere, Cone}
        projection_name (str): Name associated with this projection visualization. Should be unique!
        projection_radius (float): Radius of the generated projection visualization overall volume
            (specified in local frame)
        projection_height (float): Height of the generated projection visualization overall volume
            (specified in local frame)
        particle_radius (float): Radius of the particles composing the projection visualization
        parent_scale (3-array): If specified, specifies the (x,y,z) scale of the parent Xform prim of the
            generated source sphere prim at @prim_path. This will be used to scale the visualization accordingly
        material (None or MaterialPrim): If specified, specifies the material to associate with the generated
            particles within the projection visualization

    Returns:
        2-tuple:
            - UsdPrim: Generated ParticleSystem (ComputeGraph) prim generated
            - UsdPrim: Generated Emitter (ComputeGraph) prim generated
    """
    # Create the desired shape which will be used as the source input prim into the generated projection visualization
    source = UsdGeom.Sphere.Define(og.sim.stage, Sdf.Path(prim_path))

    # Modify the radius according to the desired @shape (and also infer the desired spread values)
    if shape == "Cylinder":
        source_radius = projection_radius
        spread = np.zeros(3)
    elif shape == "Cone":
        # Default to close to singular point otherwise
        source_radius = m.PROJECTION_VISUALIZATION_CONE_TIP_RADIUS
        spread_ratio = projection_radius * 2.0 / projection_height
        spread = np.ones(3) * spread_ratio * m.PROJECTION_VISUALIZATION_SPREAD_FACTOR
    else:
        raise ValueError(f"Invalid shape specified for projection visualization! Valid options are: [Cone, Cylinder], got: {shape}")
    # Set the radius
    source.GetRadiusAttr().Set(source_radius)
    # Also make the prim invisible
    UsdGeom.Imageable(source.GetPrim()).MakeInvisible()
    # Generate the ComputeGraph nodes to render the projection
    core = Core(lambda val: None, particle_system_name=projection_name)

    # Scale radius and height by the parent scale -- projection always points in the negative-z direction of the
    # parent frame
    # We do this AFTER we create the source sphere because the actual projection is scaled in the world frame, whereas
    # the source sphere is already scaled by its own parent frame
    # NOTE: The generated projection visualization will NOT match the underlying projection mesh if the parent link is
    # scaled non-uniformly!!
    projection_radius *= np.mean(parent_scale[:2])
    projection_height *= parent_scale[2]

    # Suppress omni warnings here -- we don't have control over this API, but omni likes to complain about this
    with suppress_omni_log(channels=["omni.graph.core.plugin", "omni.usd", "rtx.neuraylib.plugin"]):
        system_path, _, emitter_path, vis_path, instancer_path, sprite_path, mat_path, output_path = \
            core.create_particle_system(display="point_instancer", paths=[prim_path])

    # Override the prototype with our own sphere with optional material
    prototype_path = "/".join(sprite_path.split("/")[:-1]) + "/prototype"
    create_primitive_mesh(prototype_path, primitive_type="Sphere")
    prototype = VisualGeomPrim(prim_path=prototype_path, name=f"{projection_name}_prototype")
    prototype.initialize()
    # Set the scale (native scaling --> radius 0.5) and possibly update the material
    prototype.scale = particle_radius * 2.0
    if material is not None:
        prototype.material = material
    # Override the prototype used by the instancer
    instancer_prim = get_prim_at_path(instancer_path)
    instancer_prim.GetProperty("inputs:prototypes").SetTargets([prototype_path])

    # Destroy the old mat path since we don't use the sprites
    delete_prim(mat_path)

    # Modify the settings of the emitter to match the desired shape from inputs
    emitter_prim = get_prim_at_path(emitter_path)
    emitter_prim.GetProperty("inputs:active").Set(True)
    emitter_prim.GetProperty("inputs:rate").Set(m.PROJECTION_VISUALIZATION_RATE)
    emitter_prim.GetProperty("inputs:lifespan").Set(projection_height / m.PROJECTION_VISUALIZATION_SPEED)
    emitter_prim.GetProperty("inputs:speed").Set(m.PROJECTION_VISUALIZATION_SPEED)
    emitter_prim.GetProperty("inputs:alongAxis").Set(m.PROJECTION_VISUALIZATION_ORIENTATION_BIAS)
    emitter_prim.GetProperty("inputs:scale").Set(Gf.Vec3f(1.0, 1.0, 1.0))
    emitter_prim.GetProperty("inputs:directionRandom").Set(Gf.Vec3f(*spread))
    emitter_prim.GetProperty("inputs:addSourceVelocity").Set(1.0)

    # Make sure we render 4 times to fully propagate changes (validated empirically)
    # Omni likes to complain here again, but we have no control over the low-level information, so we suppress warnings
    with suppress_omni_log(channels=["omni.particle.system.core.plugin", "omni.hydra.scene_delegate.plugin", "omni.usd"]):
        for i in range(4):
            og.sim.render()

    # Return the particle system prim which "owns" everything
    return get_prim_at_path(system_path), emitter_prim


class ParticleModifier(IntrinsicObjectState, LinkBasedStateMixin, UpdateStateMixin):
    """
    Object state representing an object that has the ability to modify visual and / or physical particles within the
    active simulation.

    Args:
        obj (StatefulObject): Object to which this state will be applied
        conditions (dict): Dictionary mapping the names of ParticleSystem (str) to None or list of 2-tuples, where
            None represents no conditions, or each 2-tuple is interpreted as a single condition in the form of
            (ParticleModifyCondition, value) necessary in order for this particle modifier to be
            able to modify particles belonging to @ParticleSystem. Expected types of val are as follows:

            SATURATED: string name of the desired system that this modifier must be saturated by, e.g., "water"
            TOGGLEDON: boolean T/F; whether this modifier must be toggled on or not
            GRAVITY: boolean T/F; whether this modifier must be pointing downwards (T) or upwards (F)
            FUNCTION: a function, whose signature is as follows:

                def condition(obj) --> bool

                Where @obj is the specific object that this ParticleModifier state belongs to.

            For a given ParticleSystem, the list of 2-tuples will be converted into a list of function calls of the
            form above -- if all of its conditions evaluate to True and particles are detected within
            this particle modifier area, then we potentially modify those particles
        method (ParticleModifyMethod): Method to modify particles. Current options supported are ADJACENCY (i.e.:
            "touching" particles) or PROJECTION (i.e.: "spraying" particles)
        projection_mesh_params (None or dict): If specified and @method is ParticleModifyMethod.PROJECTION,
            manually overrides any data inferred directly from this object to infer what projection volume to generate
            for this particle modifier. Expected entries are as follows:

                "type": (str), one of {"Cylinder", "Cone", "Cube", "Sphere"}
                "extents": (3-array), the (x,y,z) extents of the generated volume (specified in local link frame!)

            If None, information found from @obj.metadata will be used instead.
            NOTE: x-direction should align with the projection mesh's height (i.e.: z) parameter in @extents!
    """
    def __init__(self, obj, conditions, method=ParticleModifyMethod.ADJACENCY, projection_mesh_params=None):

        # Store internal variables
        self.method = method
        self.projection_source_sphere = None
        self.projection_mesh = None
        self._check_in_mesh = None
        self._check_overlap = None
        self._link_prim_paths = None
        self._current_step = None
        self._projection_mesh_params = projection_mesh_params

        # Parse conditions
        self.conditions = self._parse_conditions(conditions=conditions)

        # Run super method
        super().__init__(obj)

    @classmethod
    def is_compatible(cls, obj, **kwargs):
        # Run super first
        compatible, reason = super().is_compatible(obj, **kwargs)
        if not compatible:
            return compatible, reason

        # Check whether this state has toggledon if required or saturated if required for any condition
        conditions = kwargs.get("conditions", dict())
        cond_types = {cond[0] for _, conds in conditions.items() for cond in conds}
        for cond_type, state_type in zip((ParticleModifyCondition.TOGGLEDON,), (ToggledOn,)):
            if cond_type in cond_types and state_type not in obj.states:
                return False, f"{cls.__name__} requires {state_type.__name__} state!"

        return True, None

    @classmethod
    def is_compatible_asset(cls, prim, **kwargs):
        # Run super first
        compatible, reason = super().is_compatible_asset(prim, **kwargs)
        if not compatible:
            return compatible, reason

        # Check whether this state has toggledon if required or saturated if required for any condition
        conditions = kwargs.get("conditions", dict())
        cond_types = {cond[0] for _, conds in conditions.items() for cond in conds}
        for cond_type, state_type in zip((ParticleModifyCondition.TOGGLEDON,), (ToggledOn,)):
            if cond_type in cond_types and not state_type.is_compatible_asset(prim=prim, **kwargs):
                return False, f"{cls.__name__} requires {state_type.__name__} state!"

        return True, None

    def _initialize(self):
        super()._initialize()

        # Run link initialization
        self.initialize_link_mixin()

        # Initialize internal variables
        self._current_step = 0

        # Grab link prim paths and potentially update projection mesh params
        self._link_prim_paths = set(self.obj.link_prim_paths)

        # Define callback used during overlap method
        # We want to ignore any hits that are with this object itself
        valid_hit = False
        def overlap_callback(hit):
            nonlocal valid_hit
            valid_hit = hit.rigid_body not in self._link_prim_paths
            # Continue traversal only if we don't have a valid hit yet
            return not valid_hit

        # Possibly create a projection volume if we're using the projection method
        if self.method == ParticleModifyMethod.PROJECTION:
            # Construct naming prefix to apply to generated prims
            name_prefix = f"{self.obj.name}_{self.__class__.__name__}"
            shape_defaults = {
                "radius": 0.5,
                "height": 1.0,
                "size": 1.0,
            }
            mesh_prim_path = f"{self.link.prim_path}/mesh_0"

            # Create a primitive shape if it doesn't already exist
            pre_existing_mesh = get_prim_at_path(mesh_prim_path)
            if not pre_existing_mesh:
                # Projection mesh params must be specified in order to determine scalings
                assert self._projection_mesh_params is not None, \
                    f"Must specify projection_mesh_params for {self.obj.name}'s {self.__class__.__name__} " \
                    f"since it has no pre-existing projection mesh!"
                mesh = UsdGeom.__dict__[self._projection_mesh_params["type"]].Define(og.sim.stage, mesh_prim_path).GetPrim()
                property_names = set(mesh.GetPropertyNames())
                for shape_attr, default_val in shape_defaults.items():
                    if shape_attr in property_names:
                        mesh.GetAttribute(shape_attr).Set(default_val)
            else:
                # Potentially populate projection mesh params if the prim exists
                mesh_type = pre_existing_mesh.GetTypeName()
                if self._projection_mesh_params is None:
                    self._projection_mesh_params = {
                        "type": mesh_type,
                        "extents": np.array(pre_existing_mesh.GetAttribute("xformOp:scale").Get()),
                    }
                # Otherwise, make sure we don't have a mismatch between the pre-existing shape type and the
                # desired type since we can't delete the original mesh
                else:
                    assert self._projection_mesh_params["type"] == mesh_type, \
                        f"Got mismatch in requested projection mesh type ({self._projection_mesh_params['type']}) and " \
                        f"pre-existing mesh type ({mesh_type})"

            # Create the visual geom instance referencing the generated mesh prim, and then hide it
            self.projection_mesh = VisualGeomPrim(prim_path=mesh_prim_path, name=f"{name_prefix}_projection_mesh")
            self.projection_mesh.initialize()
            self.projection_mesh.visible = False

            # Make sure the shape-based attributes are not set, and only the scaling is set
            property_names = set(self.projection_mesh.prim.GetPropertyNames())
            for shape_attr, default_val in shape_defaults.items():
                if shape_attr in property_names:
                    val = self.projection_mesh.get_attribute(shape_attr)
                    assert val == default_val, \
                        f"Projection mesh should have shape-based attribute {shape_attr} == {default_val}! Got: {val}"

            # Set the scale based on projection mesh params
            self.projection_mesh.scale = np.array(self._projection_mesh_params["extents"])

            # Make sure the object updates its meshes, and assert that there's only a single visual mesh
            self.link.update_meshes()
            assert len(self.link.visual_meshes) == 1, \
                f"Expected only a single projection mesh for {self.link}, got: {len(self.link.visual_meshes)}"

            # Make sure the mesh is translated so that its tip lies at the metalink origin, and rotated so the vector
            # from tip to tail faces the positive x axis
            z_offset = 0.0 if self._projection_mesh_params["type"] == "Sphere" else self._projection_mesh_params["extents"][2] / 2

            self.projection_mesh.set_local_pose(
                translation=np.array([0, 0, -z_offset]),
                orientation=T.euler2quat([0, 0, 0]),
            )

            # Generate the function for checking whether points are within the projection mesh
            self._check_in_mesh, _ = generate_points_in_volume_checker_function(obj=self.obj, volume_link=self.link)

            # Store the projection mesh's IDs
            projection_mesh_ids = PhysicsSchemaTools.encodeSdfPath(self.projection_mesh.prim_path)

            # We also generate the function for checking overlaps at runtime
            def check_overlap():
                nonlocal valid_hit
                valid_hit = False
                og.sim.psqi.overlap_shape(*projection_mesh_ids, reportFn=overlap_callback)
                return valid_hit

        elif self.method == ParticleModifyMethod.ADJACENCY:
            # Define the function for checking whether points are within the adjacency mesh
            def check_in_adjacency_mesh(particle_positions):
                # Define the AABB bounds
                lower, upper = self.link.aabb
                # Add the margin
                lower -= m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN
                upper += m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN
                return ((lower < particle_positions) & (particle_positions < upper)).all(axis=-1)
            self._check_in_mesh = check_in_adjacency_mesh

            # Define the function for checking overlaps at runtime
            def check_overlap():
                nonlocal valid_hit
                valid_hit = False
                aabb = self.link.aabb
                og.sim.psqi.overlap_box(
                    halfExtent=(aabb[1] - aabb[0]) / 2.0 + m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN,
                    pos=(aabb[1] + aabb[0]) / 2.0,
                    rot=np.array([0, 0, 0, 1.0]),
                    reportFn=overlap_callback,
                )
                return valid_hit

        else:
            raise ValueError(f"Unsupported ParticleModifyMethod: {self.method}!")

        # Store check overlap function
        self._check_overlap = check_overlap

        # Set saturation limits
        for system_name in self.conditions.keys():
            system = get_system(system_name, force_active=False)
            self.obj.states[Saturated].set_limit(system=system, limit=self.visual_particle_modification_limit if
            is_visual_particle_system(system_name=system.name) else self.physical_particle_modification_limit)

    def _generate_condition(self, condition_type, value):
        """
        Generates a valid condition function given @condition_type and its corresponding @value

        Args:
            condition_type (ParticleModifyCondition): Type of condition to generate
            value (any): Corresponding value whose type depends on @condition_type:

                SATURATED: string name of the desired system that this modifier must be saturated by, e.g., "water"
                TOGGLEDON: boolean T/F; whether this modifier must be toggled on or not
                GRAVITY: boolean T/F; whether this modifier must be pointing downwards (T) or upwards (F)
                FUNCTION: a function, whose signature is as follows:

                    def condition(obj) --> bool

                    Where @obj is the specific object that this ParticleModifier state belongs to.

        Returns:
            function: Condition function whose signature is identical to FUNCTION listed above
        """
        # Avoid circular imports
        from omnigibson.object_states.saturated import Saturated
        if condition_type == ParticleModifyCondition.FUNCTION:
            cond = value
        elif condition_type == ParticleModifyCondition.SATURATED:
            cond = lambda obj: is_system_active(value) and obj.states[Saturated].get_value(get_system(value))
        elif condition_type == ParticleModifyCondition.TOGGLEDON:
            cond = lambda obj: obj.states[ToggledOn].get_value() == value
        elif condition_type == ParticleModifyCondition.GRAVITY:
            # Particles spawn in negative z-axis direction, so check positive dot product of link frame with global
            cond = lambda obj: (np.dot(T.quat2mat(obj.states[self.__class__].link.get_orientation()) @ np.array([0, 0, 1]), np.array([0, 0, 1])) > 0) == value
        else:
            raise ValueError(f"Got invalid ParticleModifyCondition: {condition_type}")
        return cond

    def _parse_conditions(self, conditions):
        """
        Parse conditions and store them internally

        Args:
            conditions (dict): Dictionary mapping the names of ParticleSystem (str) to None or list of 2-tuples, where
                None represents no conditions, or each 2-tuple is interpreted as a single condition in the form of
                (ParticleModifyCondition, value) necessary in order for this particle modifier to be
                able to modify particles belonging to @ParticleSystem. Expected types of val are as follows:

                SATURATED: string name of the desired system that this modifier must be saturated by, e.g., "water"
                TOGGLEDON: boolean T/F; whether this modifier must be toggled on or not
                GRAVITY: boolean T/F; whether this modifier must be pointing downwards (T) or upwards (F)
                FUNCTION: a function, whose signature is as follows:

                    def condition(obj) --> bool

                    Where @obj is the specific object that this ParticleModifier state belongs to.

                For a given ParticleSystem, the list of 2-tuples will be converted into a list of function calls of the
                form above -- if all of its conditions evaluate to True and particles are detected within
                this particle modifier area, then we potentially modify those particles

        Returns:
            dict: Dictionary mapping the names of ParticleSystem (str) to list of condition functions
        """
        parsed_conditions = dict()
        # Standardize the conditions (make sure every system has at least one condition, which to make sure
        # the particle modifier isn't already limited with the specific number of particles)
        for system_name, conds in conditions.items():
            # Make sure the system is supported
            assert is_visual_particle_system(system_name) or is_physical_particle_system(system_name), \
                f"Unsupported system for ParticleModifier: {system_name}"
            # Make sure conds isn't empty and is a list
            conds = [] if conds is None else list(conds)
            system_conditions = []
            for cond_type, cond_val in conds:
                cond = self._generate_condition(condition_type=cond_type, value=cond_val)
                system_conditions.append(cond)
            # Always add limit condition at the end
            system_conditions.append(self._generate_limit_condition(system_name))
            parsed_conditions[system_name] = system_conditions

        return parsed_conditions

    @abstractmethod
    def _modify_particles(self, system):
        """
        Helper function to modify any particles belonging to @system.

        NOTE: This should handle both cases for @self.method:

            ParticleModifyMethod.ADJACENCY: modify any particles that are overlapping within the relaxed AABB
                defining adjacency to this object's modification link.
            ParticleModifyMethod.PROJECTION: modify any particles that are overlapping within the projection mesh.

        Must be implemented by subclass.

        Args:
            system (BaseSystem): Particle system whose corresponding particles will be checked for modification
        """
        raise NotImplementedError()

    def _generate_limit_condition(self, system_name):
        """
        Generates a limit function condition for specific system of name @system_name

        Args:
             system_name (str): Name of the particle system for which to generate a limit checker function

        Returns:
            function: Limit checker function, with signature condition(obj) --> bool, where @obj is the specific object
                that this ParticleModifier state belongs to
        """
        system = get_system(system_name, force_active=False)
        def condition(obj):
            return not self.obj.states[Saturated].get_value(system=system)

        return condition

    def _update(self):
        # If we're using projection method and flatcache, we need to manually update this object's transforms on the USD
        # so the corresponding visualization and overlap meshes are updated properly
        if self.method == ParticleModifyMethod.PROJECTION and gm.ENABLE_FLATCACHE:
            FlatcacheAPI.sync_raw_object_transforms_in_usd(prim=self.obj)

        # Check if there's any overlap and if we're at the correct step
        if self._current_step == 0 and self._check_overlap():
            # Iterate over all owned systems for this particle modifier
            for system_name, conditions in self.conditions.items():
                # Check if the system is active (for ParticleApplier, the system is always active)
                if is_system_active(system_name):
                    # Check if all conditions are met
                    if np.all([condition(self.obj) for condition in conditions]):
                        system = get_system(system_name)
                        # Sanity check for oversaturation
                        self.obj.states[Saturated].get_value(system=system)
                        # Potentially modify particles within the volume
                        self._modify_particles(system=system)

        # Update the current step
        self._current_step = (self._current_step + 1) % self.n_steps_per_modification

    @classmethod
    def get_dependencies(cls):
        deps = super().get_dependencies()
        deps.update({AABB, Saturated, ModifiedParticles})
        return deps

    @classmethod
    def get_optional_dependencies(cls):
        deps = super().get_optional_dependencies()
        deps.update({Covered, ToggledOn, ContactBodies, ContactParticles})
        return deps

    @classproperty
    def supported_active_systems(cls):
        """
        Returns:
            list: All systems used in this state that are active, dynamic across time
        """
        return list(VisualParticleSystem.get_active_systems().values()) + list(PhysicalParticleSystem.get_active_systems().values())

    @property
    def n_steps_per_modification(self):
        """
        Returns:
            int: How many steps to take in between potentially modifying particles within the simulation
        """
        raise NotImplementedError()

    @property
    def visual_particle_modification_limit(self):
        """
        Returns:
            int: Maximum number of visual particles from a specific system that can be modified by this object
        """
        raise NotImplementedError()

    @property
    def physical_particle_modification_limit(self):
        """
        Returns:
            int: Maximum number of physical particles from a specific system that can be modified by this object
        """
        raise NotImplementedError()

    @property
    def state_size(self):
        # Only store the current_step
        return 1

    def _dump_state(self):
        return dict(current_step=int(self._current_step))

    def _load_state(self, state):
        self._current_step = state["current_step"]

    def _serialize(self, state):
        return np.array([state["current_step"]], dtype=float)

    def _deserialize(self, state):
        current_step = int(state[0])
        state_dict = dict(current_step=current_step)

        return state_dict, 1

    @classproperty
    def _do_not_register_classes(cls):
        # Don't register this class since it's an abstract template
        classes = super()._do_not_register_classes
        classes.add("ParticleModifier")
        return classes


class ParticleRemover(ParticleModifier):
    """
    ParticleModifier where the modification results in potentially removing particles from the simulation.

    Args:
        obj (StatefulObject): Object to which this state will be applied
        conditions (dict): Dictionary mapping the names of ParticleSystem (str) to None or list of 2-tuples, where
            None represents no conditions, or each 2-tuple is interpreted as a single condition in the form of
            (ParticleModifyCondition, value) necessary in order for this particle modifier to be
            able to modify particles belonging to @ParticleSystem. Expected types of val are as follows:

            SATURATED: string name of the desired system that this modifier must be saturated by, e.g., "water"
            TOGGLEDON: boolean T/F; whether this modifier must be toggled on or not
            GRAVITY: boolean T/F; whether this modifier must be pointing downwards (T) or upwards (F)
            FUNCTION: a function, whose signature is as follows:

                def condition(obj) --> bool

                Where @obj is the specific object that this ParticleModifier state belongs to.

            For a given ParticleSystem, the list of 2-tuples will be converted into a list of function calls of the
            form above -- if all of its conditions evaluate to True and particles are detected within
            this particle modifier area, then we potentially modify those particles
        method (ParticleModifyMethod): Method to modify particles. Current options supported are ADJACENCY (i.e.:
            "touching" particles) or PROJECTION (i.e.: "spraying" particles)
        projection_mesh_params (None or dict): If specified and @method is ParticleModifyMethod.PROJECTION,
            manually overrides any data inferred directly from this object to infer what projection volume to generate
            for this particle modifier. Expected entries are as follows:

                "type": (str), one of {"Cylinder", "Cone", "Cube", "Sphere"}
                "extents": (3-array), the (x,y,z) extents of the generated volume (specified in local link frame!)

            If None, information found from @obj.metadata will be used instead.
            NOTE: x-direction should align with the projection mesh's height (i.e.: z) parameter in @extents!
        default_physical_conditions (None or list): Condition(s) needed to remove any physical particles not explicitly
            specified in @conditions. If None, then it is assumed that no other physical particles can be removed. If
            not None, should be in same format as an entry in @conditions, i.e.: list of (ParticleModifyCondition, val)
            2-tuples
        default_visual_conditions (None or list): Condition(s) needed to remove any visual particles not explicitly
            specified in @conditions. If None, then it is assumed that no other visual particles can be removed. If
            not None, should be in same format as an entry in @conditions, i.e.: list of (ParticleModifyCondition, val)
            2-tuples
    """
    def __init__(
        self,
        obj,
        conditions,
        method=ParticleModifyMethod.ADJACENCY,
        projection_mesh_params=None,
        default_physical_conditions=None,
        default_visual_conditions=None,
    ):
        # Store values
        self._default_physical_conditions = default_physical_conditions if default_physical_conditions is None else \
            [self._generate_condition(cond_type, cond_val) for cond_type, cond_val in default_physical_conditions]
        self._default_visual_conditions = default_visual_conditions if default_visual_conditions is None else \
            [self._generate_condition(cond_type, cond_val) for cond_type, cond_val in default_visual_conditions]

        # Run super
        super().__init__(obj=obj, conditions=conditions, method=method, projection_mesh_params=projection_mesh_params)

    def _parse_conditions(self, conditions):
        # Run super first
        parsed_conditions = super()._parse_conditions(conditions=conditions)

        # Create set of default system to condition mappings based on settings
        all_conditions = dict()
        for system_name in REGISTERED_SYSTEMS.keys():
            if is_physical_particle_system(system_name):
                default_system_conditions = self._default_physical_conditions
            elif is_visual_particle_system(system_name):
                default_system_conditions = self._default_visual_conditions
            else:
                # Don't process any other systems, continue
                continue
            if default_system_conditions is not None:
                all_conditions[system_name] = default_system_conditions + [self._generate_limit_condition(system_name)]

        # Overwrite conditions based on manually-specified ones
        all_conditions.update(parsed_conditions)

        return all_conditions

    def _modify_particles(self, system):
        # If at the limit, return
        if self.obj.states[Saturated].get_value(system=system):
            return

        # If the system has no particles, return
        if system.n_particles == 0:
            return

        # Check the system
        if is_visual_particle_system(system_name=system.name):
            # Iterate over all particles and remove any that are within the relaxed AABB of the remover volume
            particle_positions = system.get_particles_position_orientation()[0]
            inbound_idxs = self._check_in_mesh(particle_positions).nonzero()[0]
            modification_limit = self.visual_particle_modification_limit

        # Physical system
        else:
            # If the object is a cloth, we have to use check_in_mesh with the relaxed AABB since we can't detect
            # collisions via scene query interface. Alternatively, if we're using the projection method,
            # we also need to use check_in_mesh to check for overlap with the projection mesh.
            inbound_idxs = self._check_in_mesh(system.get_particles_position_orientation()[0]).nonzero()[0] \
                if self.obj.prim_type == PrimType.CLOTH or self.method == ParticleModifyMethod.PROJECTION else \
                np.array(list(self.obj.states[ContactParticles].get_value(system, self.link)))
            modification_limit = self.physical_particle_modification_limit

        n_modified_particles = self.obj.states[ModifiedParticles].get_value(system)
        n_particles_absorbed = min(len(inbound_idxs), modification_limit - n_modified_particles)
        system.remove_particles(inbound_idxs[:n_particles_absorbed])
        self.obj.states[ModifiedParticles].set_value(system, n_modified_particles + n_particles_absorbed)

    @classproperty
    def metalink_prefix(cls):
        return m.REMOVAL_LINK_PREFIX

    @classmethod
    def requires_metalink(cls, **kwargs):
        # No metalink required for adjacency
        return kwargs.get("method", ParticleModifyMethod.ADJACENCY) != ParticleModifyMethod.ADJACENCY

    @property
    def _default_link(self):
        # Only supported for adjacency, NOT projection
        return self.obj.root_link if self.method == ParticleModifyMethod.ADJACENCY else None

    @property
    def n_steps_per_modification(self):
        return m.N_STEPS_PER_REMOVAL

    @property
    def visual_particle_modification_limit(self):
        return m.VISUAL_PARTICLES_REMOVAL_LIMIT

    @property
    def physical_particle_modification_limit(self):
        return m.PHYSICAL_PARTICLES_REMOVAL_LIMIT


class ParticleApplier(ParticleModifier):
    """
    ParticleModifier where the modification results in potentially adding particles into the simulation.

    Args:
        obj (StatefulObject): Object to which this state will be applied
        conditions (dict): Dictionary mapping the names of ParticleSystem (str) to None or list of 2-tuples, where
            None represents no conditions, or each 2-tuple is interpreted as a single condition in the form of
            (ParticleModifyCondition, value) necessary in order for this particle modifier to be
            able to modify particles belonging to @ParticleSystem. Expected types of val are as follows:

            SATURATED: string name of the desired system that this modifier must be saturated by, e.g., "water"
            TOGGLEDON: boolean T/F; whether this modifier must be toggled on or not
            GRAVITY: boolean T/F; whether this modifier must be pointing downwards (T) or upwards (F)
            FUNCTION: a function, whose signature is as follows:

                def condition(obj) --> bool

                Where @obj is the specific object that this ParticleModifier state belongs to.

            For a given ParticleSystem, the list of 2-tuples will be converted into a list of function calls of the
            form above -- if all of its conditions evaluate to True and particles are detected within
            this particle modifier area, then we potentially modify those particles
        method (ParticleModifyMethod): Method to modify particles. Current options supported are ADJACENCY (i.e.:
            "touching" particles) or PROJECTION (i.e.: "spraying" particles)
        projection_mesh_params (None or dict): If specified and @method is ParticleModifyMethod.PROJECTION,
            manually overrides any data inferred directly from this object to infer what projection volume to generate
            for this particle modifier. Expected entries are as follows:

                "type": (str), one of {"Cylinder", "Cone", "Cube", "Sphere"}
                "extents": (3-array), the (x,y,z) extents of the generated volume (specified in local link frame!)

            If None, information found from @obj.metadata will be used instead.
        sample_with_raycast (bool): If True, will only sample particles at raycast hits. Otherwise, will bypass sampling
            and immediately sample particles at the sampled particle locations. Note that this will only work
            for PhysicalParticleSystem-based ParticleAppliers that use the Projection method!
        initial_speed (float): For physical particles, the initial speed for generated particles. Note that the
            direction of the velocity is inferred from the particle sampling process.
        """

    def __init__(
        self,
        obj,
        conditions,
        method=ParticleModifyMethod.ADJACENCY,
        projection_mesh_params=None,
        sample_with_raycast=True,
        initial_speed=0.0,
    ):
        # Store internal value
        self._sample_particle_locations = None
        self._sample_with_raycast = sample_with_raycast
        self._initial_speed = initial_speed

        # Pre-cached values for where particles should be spawned, and in what direction, when this state is
        # initialized so we can quickly spawn them at runtime
        self._in_mesh_local_particle_positions = None
        self._in_mesh_local_particle_directions = None

        self.projection_system = None
        self.projection_emitter = None

        # Run super
        super().__init__(obj=obj, method=method, conditions=conditions, projection_mesh_params=projection_mesh_params)

    def _initialize(self):
        # First, sanity check to make sure only one system is being applied, since unlike a ParticleRemover, which
        # can potentially remove multiple types of particles, a ParticleApplier should only apply one type of particle
        assert len(self.conditions) == 1, f"A ParticleApplier can only have a single ParticleSystem associated " \
                                          f"with it! Got: {[system_name for system_name in self.conditions.keys()]}"
        # Run super
        super()._initialize()

        system_name = list(self.conditions.keys())[0]

        # get_system will initialize the system if it's not initialized already.
        system = get_system(system_name)

        if self.visualize:
            assert self._projection_mesh_params["type"] in {"Cylinder", "Cone"}, \
                f"{self.__class__.__name__} visualization only supports Cylinder and Cone types!"
            radius, height = np.mean(self._projection_mesh_params["extents"][:2]) / 2.0, self._projection_mesh_params["extents"][2]
            # Generate the projection visualization
            particle_radius = m.VISUAL_PARTICLE_PROJECTION_PARTICLE_RADIUS if \
                is_visual_particle_system(system_name=system.name) else system.particle_radius

            name_prefix = f"{self.obj.name}_{self.__class__.__name__}"
            # Create the projection visualization if it doesn't already exist, otherwise we reference it directly
            projection_name = f"{name_prefix}_projection_visualization"
            projection_path = f"/OmniGraph/{projection_name}"
            projection_visualization_path = f"{self.link.prim_path}/projection_visualization"
            if is_prim_path_valid(projection_path):
                self.projection_system = get_prim_at_path(projection_path)
                self.projection_emitter = get_prim_at_path(f"{projection_path}/emitter")
            else:
                self.projection_system, self.projection_emitter = create_projection_visualization(
                    prim_path=projection_visualization_path,
                    shape=self._projection_mesh_params["type"],
                    projection_name=projection_name,
                    projection_radius=radius,
                    projection_height=height,
                    particle_radius=particle_radius,
                    parent_scale=self.link.scale,
                    material=system.material,
                )

            # Create the visual geom instance referencing the generated source mesh prim, and then hide it
            self.projection_source_sphere = VisualGeomPrim(prim_path=projection_visualization_path, name=f"{name_prefix}_projection_source_sphere")
            self.projection_source_sphere.initialize()
            self.projection_source_sphere.visible = False
            # Rotate by 90 degrees in y-axis so that the projection visualization aligns with the projection mesh
            self.projection_source_sphere.set_local_pose(orientation=T.euler2quat([0, np.pi / 2, 0]))

            # Make sure the meta mesh is aligned with the meta link if visualizing
            # This corresponds to checking (a) position of tip of projection mesh should align with origin of
            # metalink, and (b) zero relative orientation between the metalink and the projection mesh
            local_pos, local_quat = self.projection_mesh.get_local_pose()
            assert np.all(np.isclose(local_pos + np.array([0, 0, height / 2.0]), 0.0)), \
                "Projection mesh tip should align with metalink position!"
            assert np.all(np.isclose(T.quat2euler(local_quat), 0.0)), \
                "Projection mesh orientation should align with metalink orientation!"

        # Store which method to use for sampling particle locations
        if self._sample_with_raycast:
            if self.method == ParticleModifyMethod.PROJECTION:
                self._sample_particle_locations = self._sample_particle_locations_from_projection_volume
            elif self.method == ParticleModifyMethod.ADJACENCY:
                self._sample_particle_locations = self._sample_particle_locations_from_adjacency_area
            else:
                raise ValueError(f"Unsupported ParticleModifyMethod: {self.method}!")
        else:
            # Make sure we're only using a physical particle system and the projection method
            assert issubclass(system, PhysicalParticleSystem), \
                "If not sampling with raycast, ParticleApplier only supports PhysicalParticleSystems!"
            assert self.method == ParticleModifyMethod.PROJECTION, \
                "If not sampling with raycast, ParticleApplier only supports ParticleModifyMethod.PROJECTION method!"
            # Override the check overlap function -- this now always returns True because we don't require contact with
            # anything in order to generate particles
            self._check_overlap = lambda: True
            # Compute particle spawning information once
            self._compute_particle_spawn_information(system=system)

    def _compute_particle_spawn_information(self, system):
        """
        Helper function to compute where particles should be spawned. This is to save computation time at runtime
        if @self._sample_with_raycast is False, meaning that we were deterministically sample particles.

        Args:
            system (BaseSystem): Particle system whose particles will be spawned from this ParticleApplier
        """
        # We now pre-compute local particle positions that are within the projection mesh used to infer spawn pos
        # We sample over the entire object AABB, assuming most will be filtered out
        sampling_distance = 2 * system.particle_radius
        extent = np.array(self._projection_mesh_params["extents"])
        h = extent[2]
        low, high = self.obj.aabb
        n_particles_per_axis = ((high - low) / sampling_distance).astype(int)
        assert np.all(n_particles_per_axis), f"link {self.link.name} is too small to sample any particle of radius {system.particle_radius}."
        # 1e-10 is added because the extent might be an exact multiple of particle radius
        arrs = [np.arange(lo + system.particle_radius, hi - system.particle_radius + 1e-10, system.particle_radius * 2)
                for lo, hi, n in zip(low, high, n_particles_per_axis)]
        # Generate 3D-rectangular grid of points, and only keep the ones inside the mesh
        points = np.stack([arr.flatten() for arr in np.meshgrid(*arrs)]).T
        pos, quat = self.link.get_position_orientation()
        points = points[np.where(self._check_in_mesh(points))[0]]
        # Convert the points into local frame
        points_in_local_frame = get_particle_positions_in_frame(
            pos=pos,
            quat=quat,
            scale=self.obj.scale,
            particle_positions=points,
        )
        n_max_particles = self._get_max_particles_limit_per_step(system=system)
        # Potentially sub-sample points based on max particle limit per step
        self._in_mesh_local_particle_positions = points_in_local_frame if n_max_particles > len(points) else \
            points_in_local_frame[np.random.choice(len(points_in_local_frame), n_max_particles, replace=False)]
        # Also programmatically compute the directions of each particle position -- this is the normalized
        # vector pointing from source to the particle
        projection_type = self._projection_mesh_params["type"]
        if projection_type == "Cone":
            # Particles point from source ([0, 0, 0]) to point location
            directions = np.copy(self._in_mesh_local_particle_positions)
        elif projection_type == "Cylinder":
            # All particle points in the same parallel direction towards the -z direction
            directions = np.zeros_like(self._in_mesh_local_particle_positions)
            directions[:, 2] = -h
        else:
            raise ValueError(
                "If not sampling with raycast, ParticleApplier only supports `Cone` or `Cylinder` projection types!")
        self._in_mesh_local_particle_directions = directions / np.linalg.norm(directions, axis=-1).reshape(-1, 1)

    def _update(self):
        # If we're about to check for modification, update whether it the visualization should be active or not
        if self.visualize and self._current_step == 0:
            # Only one system in our conditions, so next(iter()) suffices
            is_active = bool(np.all([condition(self.obj) for condition in next(iter(self.conditions.values()))]))
            self.projection_emitter.GetProperty("inputs:active").Set(is_active)

        # Run super
        super()._update()

    def remove(self):
        # We need to remove the projection visualization if it exists
        if self.projection_system is not None:
            delete_prim(self.projection_system.GetPrimPath().pathString)

    def _modify_particles(self, system):
        # If at the limit, don't modify anything
        if self.obj.states[Saturated].get_value(system=system):
            return

        if self._sample_with_raycast:
            # Sample potential locations to apply particles, and then apply them
            start_points, end_points = self._sample_particle_locations(system=system)
            n_samples = len(start_points)
            is_visual = is_visual_particle_system(system_name=system.name)

            if is_visual:
                group = system.get_group_name(obj=self.obj)
                # Create an attachment group if necessary
                if group not in system.groups:
                    system.create_attachment_group(obj=self.obj)
                avg_scale = np.cbrt(np.product(self.obj.scale))
                scales = system.sample_scales_by_group(group=group, n=len(start_points))
                cuboid_dimensions = scales * system.particle_object.aabb_extent.reshape(1, 3) * avg_scale
            else:
                scales = None
                cuboid_dimensions = np.zeros(3)

            # Sample the rays to see where particle can be generated
            results = sample_cuboid_on_object(
                obj=None,
                start_points=start_points.reshape(n_samples, 1, 3),
                end_points=end_points.reshape(n_samples, 1, 3),
                cuboid_dimensions=cuboid_dimensions,
                ignore_objs=[self.obj],
                hit_proportion=0.0,             # We want all hits
                cuboid_bottom_padding=macros.utils.sampling_utils.DEFAULT_CUBOID_BOTTOM_PADDING if
                is_visual else system.particle_radius,
                undo_cuboid_bottom_padding=is_visual,      # micro particles have zero cuboid dimensions so we need to maintain padding
                verify_cuboid_empty=False,
            )

            hits = [result for result in results if result[0] is not None]
            scales = [scale for scale, result in zip(scales, results) if result[0] is not None] if scales is not None else scales

            self._apply_particles_at_raycast_hits(system=system, hits=hits, scales=scales)
        else:
            self._apply_particles_in_projection_volume(system=system)

    def _apply_particles_at_raycast_hits(self, system, hits, scales=None):
        """
        Helper function to apply particles from system @system given raycast hits @hits,
        which are the filtered results from omnigibson.utils.sampling_utils.raytest_batch that include only
        the results with a valid hit

        Args:
            system (BaseSystem): System to apply particles from
            hits (list of dict): Valid hit results from a batched raycast representing locations for sampling particles
            scales (list of numpy arrays or None): None or scales of the particles that should be sampled, same length as hits
        """
        assert system.name in self.conditions, f"System {system.name} is not defined in the conditions."
        # Check the system
        n_modified_particles = self.obj.states[ModifiedParticles].get_value(system)
        if is_visual_particle_system(system_name=system.name):
            assert scales is not None, "applying visual particles at raycast hits requires scales."
            assert len(hits) == len(scales), "length of hits and scales are different when spawning visual particles."
            # Sample potential application points
            z_up = np.zeros(3)
            z_up[-1] = 1.0
            n_particles = min(len(hits), m.VISUAL_PARTICLES_APPLICATION_LIMIT - n_modified_particles)
            # Generate particle info -- maps group name to particle info for that group,
            # i.e.: positions, orientations, and link_prim_paths
            particles_info = defaultdict(lambda: defaultdict(lambda: []))
            modifier_avg_scale = np.cbrt(np.product(self.obj.scale))
            for hit, scale in zip(hits[:n_particles], scales[:n_particles]):
                # Infer which object was hit
                hit_obj = og.sim.scene.object_registry("prim_path", "/".join(hit[3].split("/")[:-1]), None)
                if hit_obj is not None:
                    # Create an attachment group if necessary
                    group = system.get_group_name(obj=hit_obj)
                    if group not in system.groups:
                        system.create_attachment_group(obj=hit_obj)
                    # Add to info
                    particles_info[group]["positions"].append(hit[0])
                    particles_info[group]["orientations"].append(hit[2])
                    # Since particles' scales are sampled with respect to the modifier object, but are being placed
                    # (in the USD hierarchy) underneath the in_contact object, we need to compensate for the relative
                    # scale differences between the two objects, so that "moving" the particle to the new object won't
                    # cause it to unexpectedly shrink / grow based on that parent's (potentially) different scale
                    particles_info[group]["scales"].append(scale * modifier_avg_scale / np.cbrt(np.product(hit_obj.scale)))
                    particles_info[group]["link_prim_paths"].append(hit[3])
            # Generate all the particles for each group
            for group, particle_info in particles_info.items():
                # Generate particles for this group
                system.generate_group_particles(
                    group=group,
                    positions=np.array(particle_info["positions"]),
                    orientations=np.array(particle_info["orientations"]),
                    scales=np.array(particles_info[group]["scales"]),
                    link_prim_paths=particle_info["link_prim_paths"],
                )
                # Update our particle count
                self.obj.states[ModifiedParticles].set_value(system, n_modified_particles + len(particle_info["link_prim_paths"]))

        # Physical system
        else:
            # Compile the particle poses to generate and sample the particles
            n_particles = min(len(hits), m.PHYSICAL_PARTICLES_APPLICATION_LIMIT - n_modified_particles)
            # Generate particles
            if n_particles > 0:
                velocities = None if self._initial_speed == 0 else -self._initial_speed * np.array([hit[1] for hit in hits[:n_particles]])
                system.generate_particles(
                    positions=np.array([hit[0] for hit in hits[:n_particles]]),
                    velocities=velocities,
                )
                # Update our particle count
                self.obj.states[ModifiedParticles].set_value(system, n_modified_particles + n_particles)

    def _apply_particles_in_projection_volume(self, system):
        """
        Helper function to apply particles form system @system within the projection volume owned by this
        ParticleApplier.

        NOTE: This function only supports PhysicalParticleSystems and ParticleModifyMethod.PROJECTION method, which
        should have been asserted during this ParticleApplier's initialize() call

        Args:
            system (BaseSystem): System to apply particles from
        """
        assert self.method == ParticleModifyMethod.PROJECTION, \
            "Can only apply particles within projection volume if ParticleModifyMethod.PROJECTION method is used!"
        assert is_physical_particle_system(system_name=system.name), \
            "Can only apply particles within projection volume if system is PhysicalParticleSystem!"

        # Transform pre-cached particle positions into the world frame
        pos, quat = self.link.get_position_orientation()
        points = get_particle_positions_from_frame(
            pos=pos,
            quat=quat,
            scale=self.obj.scale,
            particle_positions=self._in_mesh_local_particle_positions,
        )
        directions = self._in_mesh_local_particle_directions @ T.quat2mat(quat).T

        # Compile the particle poses to generate and sample the particles
        n_modified_particles = self.obj.states[ModifiedParticles].get_value(system)
        n_particles = min(len(points), m.PHYSICAL_PARTICLES_APPLICATION_LIMIT - n_modified_particles)
        # Generate particles
        if n_particles > 0:
            velocities = None if self._initial_speed == 0 else self._initial_speed * directions[:n_particles]
            system.generate_particles(
                positions=points[:n_particles],
                velocities=velocities,
            )
            # Update our particle count
            self.obj.states[ModifiedParticles].set_value(system, n_modified_particles + n_particles)

    def _sample_particle_locations_from_projection_volume(self, system):
        """
        Helper function for generating potential particle locations from projection volume

        Args:
            system (BaseSystem): System to sample potential particle positions for

        Returns:
            2-tuple:
                - (n, 3) array: Ray start points to sample
                - (n, 3) array: Ray end points to sample
        """
        # Randomly sample end points from the base of the cone / cylinder
        n_samples = self._get_max_particles_limit_per_step(system=system)
        r, h = self._projection_mesh_params["extents"][0] / 2, self._projection_mesh_params["extents"][2]
        sampled_r_theta = np.random.rand(n_samples, 2)
        sampled_r_theta = sampled_r_theta * np.array([r, np.pi * 2]).reshape(1, 2)
        # Get start, end points in local link frame, start points to end points along the -z direction
        end_points = np.stack([
            sampled_r_theta[:, 0] * np.cos(sampled_r_theta[:, 1]),
            sampled_r_theta[:, 0] * np.sin(sampled_r_theta[:, 1]),
            -h * np.ones(n_samples),
        ], axis=1)
        projection_type = self._projection_mesh_params["type"]
        if projection_type == "Cone":
            # All start points are the cone tip, which is the local link origin
            start_points = np.zeros((n_samples, 3))
        elif projection_type == "Cylinder":
            # All start points are the parallel point for their corresponding end point
            # i.e.: (x, y, 0)
            start_points = end_points + np.array([0, 0, h]).reshape(1, 3)
        else:
            # Other types not supported
            raise ValueError(f"Unsupported projection mesh type: {projection_type}!")

        # Convert sampled normalized radius and angle into 3D points
        # We convert r, theta --> 3D point in local link frame --> 3D point in global world frame
        # We also combine start and end points for efficiency when doing the transform, then split them up again
        points = np.concatenate([start_points, end_points], axis=0)
        pos, quat = self.link.get_position_orientation()
        points = get_particle_positions_from_frame(
            pos=pos,
            quat=quat,
            scale=self.obj.scale,
            particle_positions=points,
        )

        return points[:n_samples, :], points[n_samples:, :]

    def _sample_particle_locations_from_adjacency_area(self, system):
        """
        Helper function for generating potential particle locations from adjacency area

        Args:
            system (BaseSystem): System to sample potential particle positions for

        Returns:
            2-tuple:
                - (n, 3) array: Ray start points to sample
                - (n, 3) array: Ray end points to sample
        """
        # Randomly sample end points from within the object's AABB
        n_samples = self._get_max_particles_limit_per_step(system=system)
        lower, upper = self.link.aabb
        lower = lower.reshape(1, 3) - m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN
        upper = upper.reshape(1, 3) + m.PARTICLE_MODIFIER_ADJACENCY_AREA_MARGIN
        lower_upper = np.concatenate([lower, upper], axis=0)

        # Sample in all directions, shooting from the center of the link / object frame
        pos = self.link.get_position()
        start_points = np.ones((n_samples, 3)) * pos.reshape(1, 3)
        end_points = np.random.uniform(low=lower, high=upper, size=(n_samples, 3))
        sides, axes = np.random.randint(2, size=(n_samples,)), np.random.randint(3, size=(n_samples,))
        end_points[np.arange(n_samples), axes] = lower_upper[sides, axes]

        return start_points, end_points

    def _get_max_particles_limit_per_step(self, system):
        """
        Helper function for grabbing the maximum particle limit per step

        Args:
            system (BaseSystem): System for which to get max particle limit per step

        Returns:
            int: Maximum particles to apply per step for the given system @system
        """
        assert system.name in self.conditions, f"System {system.name} is not defined in the conditions."
        return m.MAX_VISUAL_PARTICLES_APPLIED_PER_STEP if is_visual_particle_system(system_name=system.name) else \
            m.MAX_PHYSICAL_PARTICLES_APPLIED_PER_STEP

    @property
    def visualize(self):
        """
        Returns:
            bool: Whether this Applier should be visualized or not
        """
        # Visualize if projection method is used
        return self.method == ParticleModifyMethod.PROJECTION

    @classproperty
    def metalink_prefix(cls):
        return m.APPLICATION_LINK_PREFIX

    @classmethod
    def requires_metalink(cls, **kwargs):
        # No metalink required for adjacency
        return kwargs.get("method", ParticleModifyMethod.ADJACENCY) != ParticleModifyMethod.ADJACENCY

    @classmethod
    def is_compatible(cls, obj, **kwargs):
        # Run super first
        compatible, reason = super().is_compatible(obj, **kwargs)
        if not compatible:
            return compatible, reason

        # Check whether GPU dynamics are enabled (necessary for this object state)
        if not gm.USE_GPU_DYNAMICS:
            return False, f"gm.USE_GPU_DYNAMICS must be True in order to use object state {cls.__name__}."

        return True, None

    @property
    def _default_link(self):
        # Only supported for adjacency, NOT projection
        return self.obj.root_link if self.method == ParticleModifyMethod.ADJACENCY else None

    @property
    def n_steps_per_modification(self):
        return m.N_STEPS_PER_APPLICATION

    @property
    def visual_particle_modification_limit(self):
        return m.VISUAL_PARTICLES_APPLICATION_LIMIT

    @property
    def physical_particle_modification_limit(self):
        return m.PHYSICAL_PARTICLES_APPLICATION_LIMIT
