"""
Helper utility functions for computing relevant object information
"""
import omnigibson as og
import numpy as np
import omnigibson.utils.transform_utils as T
from scipy.spatial.transform import Rotation as R
from omnigibson.utils.geometry_utils import get_particle_positions_from_frame


def sample_stable_orientations(obj, n_samples=10, drop_aabb_offset=0.1):
    """
    Samples random stable orientations for obj @obj by stochastically dropping the object and recording its
    resulting orientations

    Args:
        obj (BaseObject): Object whose orientations will be sampled
        n_samples (int): How many sampled orientations will be recorded
        drop_aabb_offset (float): Offset to apply in the z-direction when dropping the object

    Returns:
        n-array: (N, 4) array, where each of the N rows are sampled (x,y,z,w) stable orientations
    """
    og.sim.play()
    assert np.all(obj.scale == 1.0)
    aabb_extent = obj.aabb_extent
    radius = np.linalg.norm(aabb_extent) / 2.0
    drop_pos = np.array([0, 0, radius + drop_aabb_offset])
    center_offset = obj.get_position() - obj.aabb_center
    drop_orientations = R.random(n_samples).as_quat()
    stable_orientations = np.zeros_like(drop_orientations)
    for i, drop_orientation in enumerate(drop_orientations):
        # Sample orientation, drop, wait to stabilize, then record
        pos = drop_pos + T.quat2mat(drop_orientation) @ center_offset
        obj.set_position_orientation(pos, drop_orientation)
        obj.keep_still()
        for j in range(25):
            og.sim.step()
        stable_orientations[i] = obj.get_orientation()

    return stable_orientations


def compute_bbox_offset(obj):
    """
    Computes the base link offset of @obj, specifying the relative position of the object's bounding box center wrt to
    its root link frame, expressed in the world frame

    Args:
        obj (BaseObject): Object whose bbox offset will be computed

    Returns:
        n-array: (x,y,z) offset specifying the relative position from the root link to @obj's bounding box center
    """
    og.sim.stop()
    assert np.all(obj.scale == 1.0)
    obj.set_position_orientation(np.zeros(3), np.array([0, 0, 0, 1.0]))
    return obj.aabb_center - obj.get_position()


def compute_native_bbox_extent(obj):
    """
    Computes the native bounding box extent for @obj, which is the extent with the obj placed at (0, 0, 0) with
    orientation (0, 0, 0, 1) and scale (1, 1, 1)

    Args:
        obj (BaseObject): Object whose native bbox extent will be computed

    Returns:
        n-array: (x,y,z) native bounding box extent
    """
    og.sim.stop()
    assert np.all(obj.scale == 1.0)
    obj.set_position_orientation(np.zeros(3), np.array([0, 0, 0, 1.0]))
    return obj.aabb_extent


def compute_base_aligned_bboxes(obj):
    link_bounding_boxes = {}
    for link_name, link in obj.links.items():
        link_bounding_boxes[link_name] = {}
        for mesh_type, mesh_list in zip(("collision", "visual"), (link.collision_meshes, link.visual_meshes)):
            pts_in_link_frame = []
            for mesh_name, mesh in mesh_list.items():
                pts = mesh.get_attribute("points")
                local_pos, local_orn = mesh.get_local_pose()
                pts_in_link_frame.append(get_particle_positions_from_frame(local_pos, local_orn, mesh.scale, pts))
            pts_in_link_frame = np.concatenate(pts_in_link_frame, axis=0)
            max_pt = np.max(pts_in_link_frame, axis=0)
            min_pt = np.min(pts_in_link_frame, axis=0)
            extent = max_pt - min_pt
            center = (max_pt + min_pt) / 2.0
            transform = T.pose2mat((center, np.array([0, 0, 0, 1.0])))
            print(pts_in_link_frame.shape)
            link_bounding_boxes[link_name][mesh_type] = {
                "extent": extent,
                "transform": transform,
            }
    return link_bounding_boxes


def compute_obj_kinematic_metadata(obj):
    """
    Computes relevant kinematic metadata for @obj, such as stable_orientations, bounding box offsets,
    bounding box extents, and base_aligned_bboxes

    Args:
        obj (BaseObject): Object whose metadata will be computed

    Returns:
        dict: Relevant metadata, with the following keys:

        - "stable_orientations": 2D (N, 4)-array of sampled stable (x,y,z,w) quaternion orientations
        - "bbox_offset": (x,y,z) relative position from the root link to @obj's bounding box center
        - "native_bbox_extent": (x,y,z) native bounding box extent
        - "base_aligned_bboxes": TODO
    """
    assert og.sim.scene is not None
    assert og.sim.scene.floor_plane is not None, "An empty scene must be used in order to compute kinematic metadata!"
    assert np.all(obj.scale == 1.0), "Object must have scale [1, 1, 1] in order to compute kinematic metadata!"
    og.sim.stop()

    return {
        "stable_orientations": sample_stable_orientations(obj=obj),
        "bbox_offset": compute_bbox_offset(obj=obj),
        "native_bbox_extent": compute_native_bbox_extent(obj=obj),
        "base_aligned_bboxes": compute_base_aligned_bboxes(obj=obj),
    }
