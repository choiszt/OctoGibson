import numpy as np
from omnigibson.utils.vision_utils import segmentation_to_rgb
import cv2
from omnigibson.utils.control_utils import IKSolver
import omnigibson as og
import math
import omnigibson.utils.transform_utils as T
from scipy.spatial.transform import Rotation as R

def quaternion_multiply(q1, q2):
    # calculate the multiply of two quaternion
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return np.array([x, y, z, w])

def rotate_quaternion_xz_inverse(q):
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_z = np.array([0, np.sin(np.pi/4), 0, -np.cos(np.pi/4)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q, q_z)
    return q_rotated

def rotate_quaternion_yz(q):
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_z = np.array([np.sin(np.pi/4), 0, 0, np.cos(np.pi/4)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q, q_z)
    return q_rotated

def rotate_3(q):
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_z = np.array([-np.sin(np.pi/4), 0, 0, np.cos(np.pi/4)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q, q_z)
    return q_rotated

def rotate_all():
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_2 = np.array([0, np.sin(np.pi/4), 0, np.cos(np.pi/4)])
    q_1 = np.array([np.sin(np.pi/8), 0, 0, np.cos(np.pi/8)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q_2, q_1)
    return q_rotated

def EasyJoint(robot, max_iter=100):
    control_idx = np.concatenate([robot.trunk_control_idx, robot.arm_control_idx[robot.default_arm]]) 
    ik_solver = IKSolver(
        robot_description_path=robot.robot_arm_descriptor_yamls[robot.default_arm],
        robot_urdf_path=robot.urdf_path,
        default_joint_pos=robot.get_joint_positions()[control_idx],
        eef_name=robot.eef_link_names[robot.default_arm],
    ) 

    robot_pos = robot.get_position()
    robot_pos[0] += 2 * robot.aabb_center[0]
    joint_pos = ik_solver.solve(target_pos=robot_pos, max_iterations=max_iter)
    if joint_pos is not None:
        og.log.info("Solution found. Setting new arm configuration.")
        robot.set_joint_positions(joint_pos, indices=control_idx)
    else:
        og.log.info("EE position not reachable.")
    og.sim.step()
    return joint_pos,control_idx


def EasyCamera(robot, camera_pos):
    # For FETCH robot, the camera control idx is [3,5]
    control_idx = np.array([3,5])
    #camera pose needs to be an ndarray
    assert isinstance(camera_pos, np.ndarray)
    robot.set_joint_positions(camera_pos, indices=control_idx, drive=True)

def quaternion_to_rotation_matrix(q):
    x, y, z, w = q
    return np.array([[1 - 2*y*y - 2*z*z, 2*x*y - 2*w*z, 2*x*z + 2*w*y],
                     [2*x*y + 2*w*z, 1 - 2*x*x - 2*z*z, 2*y*z - 2*w*x],
                     [2*x*z - 2*w*y, 2*y*z + 2*w*x, 1 - 2*x*x - 2*y*y]])

def rotation_matrix_to_quaternion(R):
    # Extract the matrix elements
    r11, r12, r13 = R[0]
    r21, r22, r23 = R[1]
    r31, r32, r33 = R[2]

    # Compute the trace of the matrix
    trace = r11 + r22 + r33

    if trace > 0:
        # Case 1: trace is positive
        s = 0.5 / math.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (r32 - r23) * s
        y = (r13 - r31) * s
        z = (r21 - r12) * s
    elif r11 > r22 and r11 > r33:
        # Case 2: r11 is the largest diagonal element
        s = 2.0 * math.sqrt(1.0 + r11 - r22 - r33)
        w = (r32 - r23) / s
        x = 0.25 * s
        y = (r12 + r21) / s
        z = (r13 + r31) / s
    elif r22 > r33:
        # Case 3: r22 is the largest diagonal element
        s = 2.0 * math.sqrt(1.0 + r22 - r11 - r33)
        w = (r13 - r31) / s
        x = (r12 + r21) / s
        y = 0.25 * s
        z = (r23 + r32) / s
    else:
        # Case 4: r33 is the largest diagonal element
        s = 2.0 * math.sqrt(1.0 + r33 - r11 - r22)
        w = (r21 - r12) / s
        x = (r13 + r31) / s
        y = (r23 + r32) / s
        z = 0.25 * s

    # Return the quaternion as a tuple
    return np.array([x,y,z,w])

def rotate_camera(q):
    r1 = quaternion_to_rotation_matrix(q)
    r2 = quaternion_to_rotation_matrix(np.array([0, np.sin(np.pi/4), 0, np.cos(np.pi/4)]))
    r = r1 @ r2
    q = rotation_matrix_to_quaternion(r)
    return q

def rotate_camera_euler():
    quat = T.euler2quat([0, 0, 90])
    return quat

def rotate_vector(v, R):
    return np.dot(R, np.array(v).reshape(-1,1)).flatten()

def EasyTeleport(robot, obj):
    obj_ori = obj.get_orientation()
    obj_R = quaternion_to_rotation_matrix(obj_ori)
    unit_z = np.array([0, 0, 1])
    obj_direction = rotate_vector(unit_z, obj_R)
    obj_direction /= np.linalg.norm(obj_direction)
    obj_pos = obj.get_position()
    new_pos = obj_pos + obj_direction * 1.0  # 1 meter far away
    obj_ori[:3] *= -1
    new_ori = obj_ori
    robot.set_position_orientation(position=new_pos, orientation=new_ori)

def rotate_quaternion_xy(q):
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_z = np.array([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q, q_z)
    return q_rotated