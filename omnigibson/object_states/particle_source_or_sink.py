import numpy as np

import omnigibson as og
from omnigibson.macros import create_module_macros
from omnigibson.object_states.particle_modifier import ParticleApplier, ParticleRemover
from omnigibson.systems.system_base import is_physical_particle_system
from omnigibson.utils.constants import ParticleModifyMethod
from omnigibson.utils.python_utils import classproperty

# Create settings for this module
m = create_module_macros(module_path=__file__)

# Metalink naming prefixes
m.SOURCE_LINK_PREFIX = "particlesource"
m.SINK_LINK_PREFIX = "particlesink"

# Default radius and height
m.DEFAULT_SOURCE_RADIUS = 0.0125
m.DEFAULT_SOURCE_HEIGHT = 0.05
m.DEFAULT_SINK_RADIUS = 0.05
m.DEFAULT_SINK_HEIGHT = 0.05

# Maximum number of particles that can be sourced / sunk per step
m.MAX_SOURCE_PARTICLES_PER_STEP = 1000
m.MAX_SINK_PARTICLES_PER_STEP = 1000

# How many steps between sinking particles
m.N_STEPS_PER_SINK = 5

# Upper limit to number of particles that can be sourced / sunk globally by a single object
m.SOURCE_PARTICLES_LIMIT = 1e6
m.SINK_PARTICLES_LIMIT = 1e6


class ParticleSource(ParticleApplier):
    """
    ParticleApplier where physical particles are spawned continuously in a cylindrical fashion from the
    metalink pose.

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
        source_radius (None or float): Radius of the cylinder representing particles' spawning volume, if specified.
            If both @source_radius and @source_height are None, values will be inferred directly from the underlying
            object asset, otherwise, it will be set to a default value
        source_height (None or float): Height of the cylinder representing particles' spawning volume, if specified.
            If both @source_radius and @source_height are None, values will be inferred directly from the underlying
            object asset, otherwise, it will be set to a default value
        initial_speed (float): The initial speed for generated particles. Note that the
            direction of the velocity is inferred from the particle sampling process
    """
    def __init__(
        self,
        obj,
        conditions,
        source_radius=None,
        source_height=None,
        initial_speed=0.0,
    ):
        # Initialize variables that will be filled in at runtime
        self._n_steps_per_modification = None

        # Define projection mesh params based on input kwargs
        if source_radius is not None or source_height is not None:
            source_radius = m.DEFAULT_SOURCE_RADIUS if source_radius is None else source_radius
            source_height = m.DEFAULT_SOURCE_HEIGHT if source_height is None else source_height
            projection_mesh_params = {
                "type": "Cylinder",
                "extents": [source_radius * 2, source_radius * 2, source_height],
            }
        else:
            projection_mesh_params = None

        # Convert inputs into arguments to pass to particle applier class
        super().__init__(
            obj=obj,
            conditions=conditions,
            method=ParticleModifyMethod.PROJECTION,
            projection_mesh_params=projection_mesh_params,
            sample_with_raycast=False,
            initial_speed=initial_speed,
        )

    def _initialize(self):
        # Run super first
        super()._initialize()

        # Calculate how many steps we need in between particle cluster spawnings
        # This is equivalent to the time it takes for a generated particle to travel @source_height distance
        # Note that object state steps are discretized by og.sim.render_step
        # Note: t derived from quadratic formula: height = 0.5 g t^2 + v0 t
        # Note: height must be considered in the world frame, so we convert the distance from local into world frame
        # Extents are in local frame, so we need to convert to world frame using link scale
        distance = self.link.scale[2] * self._projection_mesh_params["extents"][2]
        t = (-self._initial_speed + np.sqrt(self._initial_speed ** 2 + 2 * og.sim.gravity * distance)) / og.sim.gravity
        self._n_steps_per_modification = np.ceil(1 + t / og.sim.get_rendering_dt()).astype(int)

    def _get_max_particles_limit_per_step(self, system):
        # Check the system
        assert is_physical_particle_system(system_name=system.name), \
            "ParticleSource only supports PhysicalParticleSystem"
        return m.MAX_SOURCE_PARTICLES_PER_STEP

    @classmethod
    def requires_metalink(cls, **kwargs):
        # Always requires metalink since projection is used
        return True

    @property
    def visualize(self):
        # Don't visualize this source
        return False

    @classproperty
    def metalink_prefix(cls):
        return m.SOURCE_LINK_PREFIX

    @property
    def n_steps_per_modification(self):
        return self._n_steps_per_modification

    @property
    def physical_particle_modification_limit(self):
        return m.SOURCE_PARTICLES_LIMIT


class ParticleSink(ParticleRemover):
    """
    ParticleRemover where physical particles are removed continuously within a cylindrical volume located
    at the metalink pose.

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
        sink_radius (None or float): Radius of the cylinder representing particles' sinking volume, if specified.
            If both @sink_radius and @sink_height are None, values will be inferred directly from the underlying
            object asset, otherwise, it will be set to a default value
        sink_height (None or float): Height of the cylinder representing particles' sinking volume, if specified.
            If both @sink_radius and @sink_height are None, values will be inferred directly from the underlying
            object asset, otherwise, it will be set to a default value

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
        sink_radius=None,
        sink_height=None,
        default_physical_conditions=None,
        default_visual_conditions=None,
    ):
        # Initialize variables that will be filled in at runtime
        self._n_steps_per_modification = None

        # Define projection mesh params based on input kwargs
        if sink_radius is not None or sink_height is not None:
            sink_radius = m.DEFAULT_SINK_RADIUS if sink_radius is None else sink_radius
            sink_height = m.DEFAULT_SINK_HEIGHT if sink_height is None else sink_height
            projection_mesh_params = {
                "type": "Cylinder",
                "extents": [sink_radius * 2, sink_radius * 2, sink_height],
            }
        else:
            projection_mesh_params = None

        # Convert inputs into arguments to pass to particle remover class
        super().__init__(
            obj=obj,
            conditions=conditions,
            method=ParticleModifyMethod.PROJECTION,
            projection_mesh_params=projection_mesh_params,
            default_physical_conditions=default_physical_conditions,
            default_visual_conditions=default_visual_conditions,
        )

    def _initialize(self):
        # Run super first
        super()._initialize()

        # Override check overlap such that it always returns True (since we are ignoring overlaps and directly
        # removing particles
        self._check_overlap = lambda: True

    def _get_max_particles_limit_per_step(self, system):
        # Check the system
        assert is_physical_particle_system(system_name=system.name), \
            "ParticleSink only supports PhysicalParticleSystem"
        return m.MAX_PHYSICAL_PARTICLES_SOURCED_PER_STEP

    @classmethod
    def requires_metalink(cls, **kwargs):
        # Always requires metalink since projection is used
        return True

    @classproperty
    def metalink_prefix(cls):
        return m.SINK_LINK_PREFIX

    @property
    def n_steps_per_modification(self):
        return m.N_STEPS_PER_SINK

    @property
    def physical_particle_modification_limit(self):
        return m.SINK_PARTICLES_LIMIT
