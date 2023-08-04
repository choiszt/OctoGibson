import numpy as np
from omnigibson.utils.vision_utils import segmentation_to_rgb
import cv2
from omnigibson.utils.control_utils import IKSolver
import omnigibson as og
import math
import omnigibson.utils.transform_utils as T
from scipy.spatial.transform import Rotation as R

def cal_dis(pos1, pos2):
    #calculate the distance between the two position
    return np.linalg.norm(pos1 - pos2)

def EasyGrasp(robot, obj, dis_threshold):
    #Grasp the robot within the distance threshold
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
    # Hold the objects
    robot_pos = robot.get_position()
    robot_pos[2] += robot.aabb_center[2]
    robot_pos[2] -=0.2
    obj.set_position(robot_pos)

def Teleport(robot, obj, pos):
    # Teleport the robot and the objects within its hands
    robot.set_position(pos)
    Hold(robot, obj)

def MoveBot(robot, pos):
    robot.set_position(pos)

def EasyDrop(obj, pos, dis_threshold):
    # Drop the objects within robot's hands
    obj_pos = obj.get_position()
    dis = cal_dis(obj_pos, pos)
    if dis < dis_threshold:
        obj.set_position(pos)
        return True
    else:
        return False

def quaternion_multiply(q1, q2):
    # calculate the multiply of two quaternion
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return np.array([x, y, z, w])

def Turn_90(robot, pos=None):
    # turn around with 90 degrees
    ori = robot.get_orientation()
    new_ori = trans_camera(ori)
    if pos:
        robot.set_position_orientation(pos, new_ori)
    else:
        robot.set_orientation(new_ori)

# class of flying camera
class Camera():
    def __init__(self,camera,position=np.array([-2.48302418,  1.55655398,  2.22882511]),orientation=np.array([ 0.56621324, -0.0712958 , -0.10258276,  0.81473692])):
        self.camera=camera
        self.camera.set_position_orientation(
        position=position,
        orientation=orientation)
        self.seglist=[]  #{seg_file_id:(obejct_name,objectclass,instance_id)}
        
    def setposition(self,position=None,orientation=None):
        if type(orientation)==np.ndarray and type(position)!=np.ndarray:
            self.camera.set_orientation(orientation)
        if type(orientation)!=np.ndarray and type(position)==np.ndarray:
            self.camera.set_position(position)
        if  type(orientation)==np.ndarray and type(position)==np.ndarray:
            self.camera.set_position_orientation(position=position,orientation=orientation)
        else:
            raise TypeError
        
    def turn_90(self):
        ori = self.camera.get_orientation()
        new_ori = trans_camera(ori)
        self.camera.set_orientation(new_ori)

    def FlyingCapture(self,iter,file_name=None):
        obs_dict = self.camera._get_obs()
        for modality in ["rgb", "depth", "seg_instance"]:
            query_name = modality
            if query_name in obs_dict:
                if modality == "rgb":
                    pass
                elif modality == "seg_instance":
                    # Map IDs to rgb
                    segimg = segmentation_to_rgb(obs_dict[query_name][0], N=256)
                    instancemap = obs_dict[query_name][1]
                    for item in instancemap:
                        triplet=(item[1].split("/")[-1],item[3],item[4])
                        task={iter:triplet}
                        self.seglist.append(task)
                        print(f"save{task}")
                elif modality == "normal":
                    # Re-map to 0 - 1 range
                    pass
                else:
                    # Depth, nothing to do here
                    pass
                if modality == "seg_instance":
                    rgbimg = cv2.cvtColor(segimg, cv2.COLOR_BGR2RGB)
                elif modality == "rgb":
                    rgbimg = cv2.cvtColor(obs_dict[query_name], cv2.COLOR_BGR2RGB)
                else:
                    rgbimg = obs_dict[query_name]

                if file_name is not None:
                    cv2.imwrite(query_name + str(file_name) + '.png', rgbimg)
                else:
                    cv2.imwrite("./"+query_name + f'{iter}.png', rgbimg)
                    print(f"save as:{query_name + f'{iter}.png'}")
        
    def Update_camera_pos(self, robot):
        pos = robot.get_position()
        cam_pos = get_camera_position(pos)
        self.camera.set_position(cam_pos)

    def Update_camera_pos_bev(self, robot):
        pos = robot.get_position()
        cam_pos = get_camera_position_bev(pos)
        self.camera.set_position(cam_pos)

def get_camera_position(p):
    p[2] += 1.2
    # p[0] += 0.2
    return p

def get_camera_position_bev(p):
    p[2] += 3
    return p

from scipy.spatial.transform import Rotation as R
def trans_camera(q):
    random_yaw = np.pi / 2
    yaw_orn = R.from_euler("Z", random_yaw)
    new_camera_orn = quaternion_multiply(yaw_orn.as_quat(), q)
    print(new_camera_orn)
    return new_camera_orn