import numpy as np
from omnigibson.utils.vision_utils import segmentation_to_rgb
import cv2
import math
from omnigibson import object_states
import random
import omnigibson.utils.transform_utils as T
from scipy.spatial.transform import Rotation as R
import json
from bddl.object_taxonomy import ObjectTaxonomy
from omnigibson.object_states.factory import (
    get_default_states,
    get_state_name,
    get_states_for_ability,
    get_states_by_dependency_order,
    get_texture_change_states,
    get_fire_states,
    get_steam_states,
    get_visual_states,
    get_texture_change_priority,
)

from action_utils import *


OBJECT_TAXONOMY = ObjectTaxonomy()

def EasyGrasp(robot, obj, dis_threshold):
    #Grasp the robot within the distance threshold
    robot_pos = robot.get_position()
    obj_pose = obj.get_position()
    dis = cal_dis(robot_pos, obj_pose)
    # if dis < dis_threshold:
    robot_pos[2] += robot.aabb_center[2]
    robot_pos[2] -=0.2
    obj.set_position(robot_pos)
    if len(robot.inventory)>1:
        raise Exception("robot carries more than 1 object!")
    robot.inventory.append(obj._name)
    print(f"now we have:{robot.inventory}")

def MoveBot(env, robot, pos):
    robot.set_position(pos)
    if robot.inventory:
        # relationship between name and variable.
        obj = robot.inventory[0]
        Hold(env, robot, obj)

def EasyDrop(robot, obj, pos, dis_threshold): #TODO possible function  EasyDrop_V2(robot,obj1, obj2, dis_threshold) (put the OBJ1 <predicate> OBJ2)
    # Drop the objects within robot's hands
    obj_pos = obj.get_position()
    dis = cal_dis(obj_pos, pos)
    obj.set_position(pos)
    if dis < dis_threshold:
        obj.set_position(pos)
        a=robot.inventory.pop()        
        print(f"the robot throw {a},now we have:{robot.inventory}")


def FlyingCapture(camera, iter, FILENAME=None, file_name=None):
    obs_dict = camera._get_obs()
    instancemap = []
    seglist = []
    for modality in ["rgb", "depth", "seg_instance"]:
        query_name = modality
        if query_name in obs_dict:
            if modality == "rgb":
                pass
            elif modality == "seg_instance":
                # Map IDs to rgb
                instancemap.append({f"/shared/liushuai/OmniGibson/{FILENAME}/"+query_name + f'{iter}.png':obs_dict[query_name][0]})
                segimg = segmentation_to_rgb(obs_dict[query_name][0], N=256)
                instancemap = obs_dict[query_name][1]
                for item in instancemap:
                    bbox_3ds=obs_dict['bbox_3d']
                    bbox_2ds=obs_dict["bbox_2d_loose"] #
                    hextuple=[f"/shared/liushuai/OmniGibson/{FILENAME}/"+query_name + f'{iter}.png',item[1].split("/")[-1],item[3],item[0],'','']
                    for bbox_2d in bbox_2ds:
                        if bbox_2d[0]==item[0]:
                            bbox2d_info=[bbox_2d[i] for i in range(6,10,1)]
                            hextuple[4]=bbox2d_info
                            break
                    for bbox_3d in bbox_3ds:
                        if bbox_3d[0]==item[0]:
                            bbox3d_info=[bbox_3d[i] for i in range(2,9,1)]
                            hextuple[5]=bbox3d_info
                            break
                    seglist.append(hextuple)
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
                cv2.imwrite(f"/shared/liushuai/OmniGibson/{FILENAME}/"+query_name + f'{iter}.png', rgbimg)
                print(f"save as:{query_name + f'{iter}.png'}")
    return instancemap, seglist

from collections import OrderedDict
def donothing(env):
    action=np.zeros(11)
    dumbact=OrderedDict([('robot0', action)])
    step=0
    for _ in range(30):
        # og.sim.step()
        env.step(dumbact)
        step += 1

reverse=lambda states:{value:key for key,value in states.items()}
unary_states={object_states.Cooked:"cooked",object_states.Burnt:"burnt",object_states.Frozen:"frozen",object_states.Heated:"hot",
                         object_states.Open:"open",object_states.ToggledOn:"toggled_on",object_states.Folded:"folded",object_states.Unfolded:"unfolded"}
binary__states={
    object_states.Inside: "inside",
    object_states.NextTo: "nextto",
    object_states.OnTop: "ontop",
    object_states.Under: "under",
    object_states.Touching: "touching",
    object_states.Covered: "covered",
    object_states.Contains: "contains",
    object_states.Saturated: "saturated",
    object_states.Filled: "filled",
    object_states.AttachedTo: "attached",
    object_states.Overlaid: "overlaid",
    object_states.Draped: "draped"
}
reversed_unary_states,reversed_binary__states=reverse(unary_states),reverse(binary__states)

def change_states(obj, states, oper):
    '''
    obj (Objects): The object that the states are needed to be changed.
    states (str): The specific states to be changed.
    oper (int): 0 or 1, meaning the False or True of the states.
    '''
    try:
        states_status=reversed_unary_states[states]
        obj.states[states_status].set_value(oper)
    except:
        print(f'Wrong state or operation {states, oper}')

def get_states(env,obj:str,state:str)->object_states:
    whole_dict={**reversed_unary_states,**reversed_binary__states}
    class_obj=env.scene.object_registry("name", obj)
    try:
        if whole_dict[state] in list(class_obj.states.keys()):
            return whole_dict[state]
        else:
            print(f"{obj} don't have states {whole_dict[state]}")
            raise Exception
    except:
        print(f"Wrong state {state}")
        raise Exception
