import numpy as np
from omnigibson.utils.vision_utils import segmentation_to_rgb
import cv2
from omnigibson.utils.control_utils import IKSolver
import omnigibson as og

def cal_dis(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)

def EasyGrasp(robot, obj, dis_threshold):
    robot_pos = robot.get_position()
    obj_pose = obj.get_position()
    dis = cal_dis(robot_pos, obj_pose)
    if dis < dis_threshold:
        robot_pos[2] += robot.aabb_center[2]
        robot_pos[2] -=0.2
        obj.set_position(robot_pos)
        return True
    else:
        return False

def Hold(robot, obj):
    robot_pos = robot.get_position()
    robot_pos[2] += robot.aabb_center[2]
    robot_pos[2] -=0.2
    obj.set_position(robot_pos)

def Teleport(robot, obj, pos):
    robot.set_position(pos)
    Hold(robot, obj)
    # TODO: robot orientation, need another obj to represent the scene we want to capture
    _, orientation = robot.get_position_orientation()
    new_orientation = orientation
    robot.set_orientation(new_orientation)

def MoveBot(robot, pos):
    robot.set_position(pos)
    # TODO: robot orientation, need another obj to represent the scene we want to capture
    _, orientation = robot.get_position_orientation()
    new_orientation = orientation
    robot.set_orientation(new_orientation)

def EasyDrop(obj, pos, dis_threshold):
    obj_pos = obj.get_position()
    dis = cal_dis(obj_pos, pos)
    if dis < dis_threshold:
        obj.set_position(pos)
        return True
    else:
        return False

def quaternion_multiply(q1, q2):
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return np.array([x, y, z, w])

def rotate_quaternion_xy(q):
    # Construct a quaternion representing a 90 degree rotation about the z-axis
    q_z = np.array([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])
    # Rotate the input quaternion by the z-axis quaternion
    q_rotated = quaternion_multiply(q, q_z)
    return q_rotated

def Turn_90(robot):
    ori = robot.get_orientation()
    new_ori = rotate_quaternion_xy(ori)
    robot.set_orientation(new_ori)

def Turn_90_PO(robot,pos):
    ori = robot.get_orientation()
    new_ori = rotate_quaternion_xy(ori)
    robot.set_position_orientation(pos,new_ori)
    
def Capture(robot,iter,file_name=None):
    obs_dict = robot.get_obs()
    for sensor_name, _ in robot._sensors.items():
        for modality in ["rgb", "depth", "normal", "seg_instance"]:
            query_name = str(sensor_name)+ '_' + modality
            
            if query_name in obs_dict:
                
                # if modality == "rgb":
                #     # Ignore alpha channel, map to floats
                #     obs_dict[query_name] = obs_dict[query_name][:, :, :3] / 255.0
                # elif modality == "seg_instance":
                #     # Map IDs to rgb
                #     obs_dict[query_name] = segmentation_to_rgb(obs_dict[query_name], N=256) / 255.0
                # elif modality == "normal":
                #     # Re-map to 0 - 1 range
                #     obs_dict[query_name] = (obs_dict[query_name] + 1.0) / 2.0
                # else:
                #     # Depth, nothing to do here
                #     pass

                if modality == "rgb":
                    pass
                elif modality == "seg_instance":
                    # Map IDs to rgb
                    segimg = segmentation_to_rgb(obs_dict[query_name][0], N=256)
                    instancemap=obs_dict[query_name][1]
                elif modality == "normal":
                    # Re-map to 0 - 1 range
                    pass
                else:
                    # Depth, nothing to do here
                    pass
                if(modality == "seg_instance"):
                    rgbimg=cv2.cvtColor(segimg, cv2.COLOR_BGR2RGB)
                else:
                    rgbimg=cv2.cvtColor(obs_dict[query_name], cv2.COLOR_BGR2RGB)
                if file_name is not None:
                    cv2.imwrite(query_name + str(file_name) + '.png', rgbimg)
                else:
                    cv2.imwrite("/shared/liushuai/OmniGibson/pic1/"+query_name + f'{iter}.png', rgbimg)
                    print(f"save as:{query_name + f'{iter}.png'}")

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