"""
A set of helper utility functions for dealing with 3D geometry
"""
import numpy as np
import omnigibson.utils.transform_utils as T
from omnigibson.utils.usd_utils import mesh_prim_to_trimesh_mesh


def get_particle_positions_in_frame(pos, quat, scale, particle_positions):
    """
    Transforms particle positions @positions into the frame specified by @pos and @quat with new scale @scale,
    where @pos and @quat are assumed to be specified in the same coordinate frame that @particle_positions is specified

    Args:
        pos (3-array): (x,y,z) pos of the new frame
        quat (4-array): (x,y,z,w) quaternion orientation of the new frame
        scale (3-array): (x,y,z) local scale of the new frame
        particle_positions ((N, 3) array): positions

    Returns:
        (N,) array: updated particle positions in the new coordinate frame
    """

    # Get pose of origin (global frame) in new_frame
    origin_in_new_frame = T.pose_inv(T.pose2mat((pos, quat)))
    # Batch the transforms to get all particle points in the local link frame
    positions_tensor = np.tile(np.eye(4).reshape(1, 4, 4), (len(particle_positions), 1, 1))  # (N, 4, 4)
    # Scale by the new scale#
    positions_tensor[:, :3, 3] = particle_positions
    particle_positions = (origin_in_new_frame @ positions_tensor)[:, :3, 3]  # (N, 3)
    # Scale by the new scale
    return particle_positions / scale.reshape(1, 3)


def get_particle_positions_from_frame(pos, quat, scale, particle_positions):
    """
    Transforms particle positions @positions from the frame specified by @pos and @quat with new scale @scale.

    This is similar to @get_particle_positions_in_frame, but does the reverse operation, inverting @pos and @quat

    Args:
        pos (3-array): (x,y,z) pos of the local frame
        quat (4-array): (x,y,z,w) quaternion orientation of the local frame
        scale (3-array): (x,y,z) local scale of the local frame
        particle_positions ((N, 3) array): positions

    Returns:
        (N,) array: updated particle positions in the parent coordinate frame
    """
    # Scale by the new scale
    particle_positions = particle_positions * scale.reshape(1, 3)

    # Get pose of origin (global frame) in new_frame
    origin_in_new_frame = T.pose2mat((pos, quat))
    # Batch the transforms to get all particle points in the local link frame
    positions_tensor = np.tile(np.eye(4).reshape(1, 4, 4), (len(particle_positions), 1, 1))  # (N, 4, 4)
    # Scale by the new scale#
    positions_tensor[:, :3, 3] = particle_positions
    return (origin_in_new_frame @ positions_tensor)[:, :3, 3]  # (N, 3)


def check_points_in_cube(size, pos, quat, scale, particle_positions):
    """
    Checks which points are within a cube with specified size @size.

    NOTE: Assumes the cube and positions are expressed
    in the same coordinate frame such that the cube's dimensions are axis-aligned with (x,y,z)

    Args:
        size float: length of each side of the cube, specified in its local frame
        pos (3-array): (x,y,z) local location of the cube
        quat (4-array): (x,y,z,w) local orientation of the cube
        scale (3-array): (x,y,z) local scale of the cube, specified in its local frame
        particle_positions ((N, 3) array): positions to check for whether it is in the cube

    Returns:
        (N,) array: boolean numpy array specifying whether each point lies in the cube.
    """
    particle_positions = get_particle_positions_in_frame(
        pos=pos,
        quat=quat,
        scale=scale,
        particle_positions=particle_positions,
    )
    return ((-size / 2.0 < particle_positions) & (particle_positions < size / 2.0)).sum(axis=-1) == 3


def check_points_in_cone(size, pos, quat, scale, particle_positions):
    """
    Checks which points are within a cone with specified size @size.

    NOTE: Assumes the cone and positions are
    expressed in the same coordinate frame such that the cone's height is aligned with the z-axis

    Args:
        size (2-array): (radius, height) dimensions of the cone, specified in its local frame
        pos (3-array): (x,y,z) local location of the cone
        quat (4-array): (x,y,z,w) local orientation of the cone
        scale (3-array): (x,y,z) local scale of the cone, specified in its local frame
        particle_positions ((N, 3) array): positions to check for whether it is in the cone

    Returns:
        (N,) array: boolean numpy array specifying whether each point lies in the cone.
    """
    particle_positions = get_particle_positions_in_frame(
        pos=pos,
        quat=quat,
        scale=scale,
        particle_positions=particle_positions,
    )
    radius, height = size
    in_height = (-height / 2.0 < particle_positions[:, -1]) & (particle_positions[:, -1] < height / 2.0)
    in_radius = np.linalg.norm(particle_positions[:, :-1], axis=-1) < \
                (radius * (1 - (particle_positions[:, -1] + height / 2.0) / height ))
    return in_height & in_radius


def check_points_in_cylinder(size, pos, quat, scale, particle_positions):
    """
    Checks which points are within a cylinder with specified size @size.

    NOTE: Assumes the cylinder and positions are
    expressed in the same coordinate frame such that the cylinder's height is aligned with the z-axis

    Args:
        size (2-array): (radius, height) dimensions of the cylinder, specified in its local frame
        pos (3-array): (x,y,z) local location of the cylinder
        quat (4-array): (x,y,z,w) local orientation of the cylinder
        scale (3-array): (x,y,z) local scale of the cube, specified in its local frame
        particle_positions ((N, 3) array): positions to check for whether it is in the cylinder

    Returns:
        (N,) array: boolean numpy array specifying whether each point lies in the cylinder.
    """
    particle_positions = get_particle_positions_in_frame(
        pos=pos,
        quat=quat,
        scale=scale,
        particle_positions=particle_positions,
    )
    radius, height = size
    in_height = (-height / 2.0 < particle_positions[:, -1]) & (particle_positions[:, -1] < height / 2.0)
    in_radius = np.linalg.norm(particle_positions[:, :-1], axis=-1) < radius
    return in_height & in_radius


def check_points_in_sphere(size, pos, quat, scale, particle_positions):
    """
    Checks which points are within a sphere with specified size @size.

    NOTE: Assumes the sphere and positions are expressed in the same coordinate frame

    Args:
        size (float): radius dimensions of the sphere
        pos (3-array): (x,y,z) local location of the sphere
        quat (4-array): (x,y,z,w) local orientation of the sphere
        scale (3-array): (x,y,z) local scale of the cube, specified in its local frame
        particle_positions ((N, 3) array): positions to check for whether it is in the sphere

    Returns:
        (N,) array: boolean numpy array specifying whether each point lies in the sphere
    """
    particle_positions = get_particle_positions_in_frame(
        pos=pos,
        quat=quat,
        scale=scale,
        particle_positions=particle_positions,
    )
    return np.linalg.norm(particle_positions, axis=-1) < size


def check_points_in_convex_hull_mesh(mesh_face_centroids, mesh_face_normals, pos, quat, scale, particle_positions):
    """
    Checks which points are within a sphere with specified size @size.

    NOTE: Assumes the mesh and positions are expressed in the same coordinate frame

    Args:
        mesh_face_centroids (D, 3): (x,y,z) location of the centroid of each mesh face, expressed in its local frame
        mesh_face_normals (D, 3): (x,y,z) normalized direction vector of each mesh face, expressed in its local frame
        pos (3-array): (x,y,z) local location of the mesh
        quat (4-array): (x,y,z,w) local orientation of the mesh
        scale (3-array): (x,y,z) local scale of the cube, specified in its local frame
        particle_positions ((N, 3) array): positions to check for whether it is in the mesh

    Returns:
        (N,) array: boolean numpy array specifying whether each point lies in the mesh
    """
    particle_positions = get_particle_positions_in_frame(
        pos=pos,
        quat=quat,
        scale=scale,
        particle_positions=particle_positions,
    )
    # For every mesh point / normal and particle position pair, we check whether it is "inside" (i.e.: the point lies
    # BEHIND the normal plane -- this is easily done by taking the dot product with the vector from the point to the
    # particle position with the normal, and validating that the value is < 0)
    D, _ = mesh_face_centroids.shape
    N, _ = particle_positions.shape
    mesh_points = np.tile(mesh_face_centroids.reshape(1, D, 3), (N, 1, 1))
    mesh_normals = np.tile(mesh_face_normals.reshape(1, D, 3), (N, 1, 1))
    particle_positions = np.tile(particle_positions.reshape(N, 1, 3), (1, D, 1))
    # All arrays are now (N, D, 3) shape -- efficient for batching
    in_range = ((particle_positions - mesh_points) * mesh_normals).sum(axis=-1) < 0         # shape (N, D)
    # All D normals must be satisfied for a single point to be considered inside the hull
    in_range = in_range.sum(axis=-1) == D
    return in_range


def _generate_convex_hull_volume_checker_functions(convex_hull_mesh):
    """
    An internal helper function used to programmatically generate lambda funtions to check for particle
    points within a convex hull mesh defined by face centroids @mesh_face_centroids and @mesh_face_normals.

    Note that this is needed as an EXTERNAL helper function to @generate_points_in_volume_checker_function
    because we "bake" certain arguments as part of the lambda internal scope, and
    directly generating functions in a for loop results in these local variables being overwritten each time
    (meaning that all the generated lambda functions reference the SAME variables!!)

    Args:
        convex_hull_mesh (Usd.Prim): Raw USD convex hull mesh to generate the volume checker functions

    Returns:
        2-tuple:
            - function: Generated lambda function with signature:

                    in_range = check_in_volume(mesh, particle_positions)

                where @in_range is a N-array boolean numpy array, (True where the particle is in the convex hull mesh
                    volume), @mesh is the raw USD mesh, and @particle_positions is a (N, 3) array specifying the particle
                    positions in the SAME coordinate frame as @mesh

            - function: Function for grabbing real-time LOCAL scale volume of the container. Signature:

                vol = calc_volume(mesh)

            where @vol is the total volume being checked (expressed in the mesh's LOCAL scale), and @mesh is the raw
                USD mesh
    """
    # For efficiency, we pre-compute the mesh using trimesh and find its corresponding faces and normals
    trimesh_mesh = mesh_prim_to_trimesh_mesh(convex_hull_mesh, include_normals=False, include_texcoord=False).convex_hull
    assert trimesh_mesh.is_convex, \
        f"Trying to generate a volume checker function for a non-convex mesh {convex_hull_mesh.GetPath().pathString}"
    face_centroids = trimesh_mesh.vertices[trimesh_mesh.faces].mean(axis=1)
    face_normals = trimesh_mesh.face_normals

    # This function assumes that:
    # 1. @particle_positions are in the local container_link frame
    # 2. the @check_points_in_[...] function will convert them into the local @mesh frame
    in_volume = lambda mesh, particle_positions: check_points_in_convex_hull_mesh(
        mesh_face_centroids=face_centroids,
        mesh_face_normals=face_normals,
        pos=np.array(mesh.GetAttribute("xformOp:translate").Get()),
        quat=np.array(
            [*(mesh.GetAttribute("xformOp:orient").Get().imaginary), mesh.GetAttribute("xformOp:orient").Get().real]),
        scale=np.array(mesh.GetAttribute("xformOp:scale").Get()),
        particle_positions=particle_positions,
    )
    calc_volume = lambda mesh: trimesh_mesh.volume if trimesh_mesh.is_volume else trimesh_mesh.convex_hull.volume
    return in_volume, calc_volume


def generate_points_in_volume_checker_function(obj, volume_link, use_visual_meshes=True, mesh_name_prefixes=None):
    """
    Generates a function for quickly checking which of a group of points are contained within any container volumes.
    Four volume types are supported:
        "Cylinder" - Cylinder volume
        "Cube" - Cube volume
        "Sphere" - Sphere volume
        "Mesh" - Convex hull volume

    @volume_link should have any number of nested, visual-only meshes of types {Sphere, Cylinder, Cube, Mesh} with
    naming prefix "container[...]"

    Args:
        obj (EntityPrim): Object which contains @volume_link as one of its links
        volume_link (RigidPrim): Link to use to grab container volumes composing the values for checking the points
        use_visual_meshes (bool): Whether to use @volume_link's visual or collision meshes to generate points fcn
        mesh_name_prefixes (None or str): If specified, specifies the substring that must exist in @volume_link's
            mesh names in order for that mesh to be included in the volume checker function. If None, no filtering
            will be used.

    Returns:
        2-tuple:
            - function: Function with signature:

                in_range = check_in_volumes(particle_positions)

            where @in_range is a N-array boolean numpy array, (True where the particle is in the volume), and
            @particle_positions is a (N, 3) array specifying the particle positions in global coordinates

            - function: Function for grabbing real-time global scale volume of the container. Signature:

                vol = total_volume()

            where @vol is the total volume being checked (expressed in global scale) aggregated across
            all container sub-volumes
    """
    # If the object doesn't uniform scale, we make sure the volume link has no relative orientation w.r.t to
    # the object (root link) frame
    # TODO: Can we remove this restriction in the future? The current paradigm of how scale operates makes this difficult
    if (obj.scale.max() - obj.scale.min()) > 1e-3:
        volume_link_quat = volume_link.get_orientation()
        object_quat = obj.get_orientation()
        quat_distance = T.quat_distance(volume_link_quat, object_quat)
        assert np.isclose(quat_distance[3], 1, atol=1e-3), \
            f"Volume link must have no relative orientation w.r.t the root link! (i.e.: quat distance [0, 0, 0, 1])! " \
            f"Got quat distance: {quat_distance}"
    # Iterate through all visual meshes and keep track of any that are prefixed with container
    container_meshes = []
    meshes = volume_link.visual_meshes if use_visual_meshes else volume_link.collision_meshes
    for container_mesh_name, container_mesh in meshes.items():
        if mesh_name_prefixes is None or mesh_name_prefixes in container_mesh_name:
            container_meshes.append(container_mesh.prim)

    # Programmatically define the volume checker functions based on each container found
    volume_checker_fcns = []
    volume_calc_fcns = []
    for sub_container_mesh in container_meshes:
        mesh_type = sub_container_mesh.GetTypeName()
        if mesh_type == "Mesh":
            fcn, vol_fcn = _generate_convex_hull_volume_checker_functions(convex_hull_mesh=sub_container_mesh)
        elif mesh_type == "Sphere":
            fcn = lambda mesh, particle_positions: check_points_in_sphere(
                size=mesh.GetAttribute("radius").Get(),
                pos=np.array(mesh.GetAttribute("xformOp:translate").Get()),
                quat=np.array([*(mesh.GetAttribute("xformOp:orient").Get().imaginary), mesh.GetAttribute("xformOp:orient").Get().real]),
                scale=np.array(mesh.GetAttribute("xformOp:scale").Get()),
                particle_positions=particle_positions,
            )
            vol_fcn = lambda mesh: 4 / 3 * np.pi * (mesh.GetAttribute("radius").Get() ** 3)
        elif mesh_type == "Cylinder":
            fcn = lambda mesh, particle_positions: check_points_in_cylinder(
                size=[mesh.GetAttribute("radius").Get(), mesh.GetAttribute("height").Get()],
                pos=np.array(mesh.GetAttribute("xformOp:translate").Get()),
                quat=np.array([*(mesh.GetAttribute("xformOp:orient").Get().imaginary), mesh.GetAttribute("xformOp:orient").Get().real]),
                scale=np.array(mesh.GetAttribute("xformOp:scale").Get()),
                particle_positions=particle_positions,
            )
            vol_fcn = lambda mesh: np.pi * (mesh.GetAttribute("radius").Get() ** 2) * mesh.GetAttribute("height").Get()
        elif mesh_type == "Cone":
            fcn = lambda mesh, particle_positions: check_points_in_cone(
                size=[mesh.GetAttribute("radius").Get(), mesh.GetAttribute("height").Get()],
                pos=np.array(mesh.GetAttribute("xformOp:translate").Get()),
                quat=np.array([*(mesh.GetAttribute("xformOp:orient").Get().imaginary), mesh.GetAttribute("xformOp:orient").Get().real]),
                scale=np.array(mesh.GetAttribute("xformOp:scale").Get()),
                particle_positions=particle_positions,
            )
            vol_fcn = lambda mesh: np.pi * (mesh.GetAttribute("radius").Get() ** 2) * mesh.GetAttribute("height").Get() / 3.0
        elif mesh_type == "Cube":
            fcn = lambda mesh, particle_positions: check_points_in_cube(
                size=mesh.GetAttribute("size").Get(),
                pos=np.array(mesh.GetAttribute("xformOp:translate").Get()),
                quat=np.array([*(mesh.GetAttribute("xformOp:orient").Get().imaginary), mesh.GetAttribute("xformOp:orient").Get().real]),
                scale=np.array(mesh.GetAttribute("xformOp:scale").Get()),
                particle_positions=particle_positions,
            )
            vol_fcn = lambda mesh: mesh.GetAttribute("size").Get() ** 3
        else:
            raise ValueError(f"Cannot create volume checker function for mesh of type: {mesh_type}")

        volume_checker_fcns.append(fcn)
        volume_calc_fcns.append(vol_fcn)

    # Define the actual volume checker function
    def check_points_in_volumes(particle_positions):
        # Algo
        # 1. Particles in global frame --> particles in volume link frame (including scaling)
        # 2. For each volume checker function, apply volume checking
        # 3. Aggregate across all functions with OR condition (any volume satisfied for that point)
        ######

        n_particles = len(particle_positions)
        # Get pose of origin (global frame) in frame of volume link
        # NOTE: This assumes there is no relative scaling between obj and volume link
        volume_link_pos, volume_link_quat = volume_link.get_position_orientation()
        particle_positions = get_particle_positions_in_frame(
            pos=volume_link_pos,
            quat=volume_link_quat,
            scale=obj.scale,
            particle_positions=particle_positions,
        )

        in_volumes = np.zeros(n_particles).astype(bool)
        for checker_fcn, mesh in zip(volume_checker_fcns, container_meshes):
            in_volumes |= checker_fcn(mesh, particle_positions)

        return in_volumes

    # Define the actual volume calculator function
    def calculate_volume():
        # Aggregate values across all subvolumes
        # NOTE: Assumes all volumes are strictly disjointed (becuase we sum over all subvolumes to calculate
        # total raw volume)
        # TODO: Is there a way we can explicitly check if disjointed?
        vols = [calc_fcn(mesh) * np.product(mesh.GetAttribute("xformOp:scale").Get())
                for calc_fcn, mesh in zip(volume_calc_fcns, container_meshes)]
        # Aggregate over all volumes and scale by the link's global scale
        return np.sum(vols) * np.product(volume_link.get_world_scale())

    return check_points_in_volumes, calculate_volume
