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



OBJECT_TAXONOMY = ObjectTaxonomy()


def cal_dis(pos1, pos2):
    #calculate the distance between the two position
    return np.linalg.norm(pos1 - pos2)

def Hold(env, robot, obj_name):
    # Hold the objects
    robot_pos = robot.get_position()
    robot_pos[2] += robot.aabb_center[2]
    robot_pos[2] -=0.2 
    obj=env.scene.object_registry("name",obj_name)  
    obj.set_position(robot_pos)

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

def getallobject(env, ):
    allobject = []
    try:
        objectlist = [i['name'] for i in env.objects_config]
    except:
        pass
    scenedict = env.scene.get_objects_info()
    scenelist = list(scenedict['init_info'].keys())
    return list(set(objectlist + scenelist))

def setposition(camera, position=None,orientation=None):
    if type(orientation)==np.ndarray and type(position)!=np.ndarray:
        camera.set_orientation(orientation)
    if type(orientation)!=np.ndarray and type(position)==np.ndarray:
        camera.set_position(position)
    if  type(orientation)==np.ndarray and type(position)==np.ndarray:
        camera.set_position_orientation(position=position,orientation=orientation)
    else:
        raise TypeError
    
def xyz2spherical(position):
    x,y,z = [position[i] for i in range(3)]
    rho = math.sqrt(x**2+y**2+z**2)
    theta = math.atan2(y,x)
    phi = math.acos(z/rho)
    #convert to degree
    theta_deg = math.degrees(theta)
    phi_deg = math.degrees(phi)
    return {"rho":rho,"theta_deg":theta_deg,"phi_deg":phi_deg}

def set_in_rob(env, allobject, robot):
    obj_in_rob={}
    for object_name in allobject:
        tempobj = env.scene.object_registry("name",object_name)
        pose_in_rob = align_coord(tempobj,robot)
        obj_in_rob[object_name]=(xyz2spherical(pose_in_rob[0]),pose_in_rob[1])
    return obj_in_rob
            
def align_coord(obj,rob):
    #choiszt convert world2bot coord
    obj_in_world = T.pose2mat(obj.get_position_orientation())
    rob_in_world = T.pose2mat(rob.get_position_orientation())
    world_in_rob = T.pose_inv(rob_in_world)
    #same with T.relative_pose_transform(tempobj.get_position(),tempobj.get_orientation(),robot.get_position(),robot.get_orientation()) ## choiszt have varified this 
    obj_in_rob = T.pose_in_A_to_pose_in_B(obj_in_world, world_in_rob)
    obj2rob =T.mat2pose(obj_in_rob)
    return obj2rob

def turn_90(camera):
    ori = camera.get_orientation()
    new_ori = trans_camera(ori)
    camera.set_orientation(new_ori)
    
def parsing_segmentdata(seglist, instancemap): #parse all data from the files that we have collected
    seglists = seglist
    instancemaps = instancemap
    parse=lambda path:list(path.keys())[0]
    nowwehave=[]
    for ele in instancemaps:
        path=parse(ele)
        templist=[]
        tempdict={}
        map=ele[path]
        instance=list(np.unique(map))
        for seglist in seglists:
            if seglist[0]==path:
                instance_id=seglist[3]
                if instance_id in instance:
                    templist.append(seglist[1])
        tempdict[path]=templist
        nowwehave.append(tempdict) #dict{path:object_name}
    print("now begin to parse segmentation data")
    return nowwehave

def parseSG(env, objects):
    blacklist=["walls","electric_switch","floors","ceilings","window"]
    pairs=[]
    SG=[]
    for i in range(len(objects)):
        for j in range(len(objects)):
            cnt=0
            if(objects[i]!=objects[j]):
                for blackele in blacklist:
                    if blackele in objects[i]:
                        cnt+=1
                    if blackele in objects[j]:
                        cnt+=1
                if cnt!=2:
                    pairs.append((objects[i],objects[j]))
    for pair in pairs:
        obj0 = env.scene.object_registry("name",pair[0])
        obj1 = env.scene.object_registry("name",pair[1])
        try:
            is_inside=obj0.states[object_states.Inside].get_value(obj1)
            if is_inside:
                SG.append((obj0._name,"inside",obj1._name))
        except:
            pass
        try:
            is_nextto=obj0.states[object_states.NextTo].get_value(obj1)
            if is_nextto:
                SG.append((obj0._name,"nextto",obj1._name))                
        except:
            pass            
        try:
            is_ontop=obj0.states[object_states.OnTop].get_value(obj1)
            if is_ontop:
                SG.append((obj0._name,"ontop",obj1._name))                   
        except:
            pass        
        try:
            is_overlaid=obj0.states[object_states.Overlaid].get_value(obj1)
            if is_overlaid:
                SG.append((obj0._name,"overlaid",obj1._name))                   
        except:
            pass        
        try:
            is_under=obj0.states[object_states.Under].get_value(obj1)
            if is_under:
                SG.append((obj0._name,"under",obj1._name))                   
        except:
            pass                                
    return {"scene_graph":SG}

def collectdata_v2(env, robot, seglist, actionlist): #each time change the robot position need to collectdata
    nowwehave=parsing_segmentdata()
    inventory=robot.inventory
    sub_nowwehave=[]
    for key in nowwehave:
        if list(key.keys())[0].split("/")[-1].rstrip('.png').lstrip("seg_instance") not in self.actionlist:
            sub_nowwehave.append(key)
    seglists=seglist
    obj_in_robs=set_in_rob(robot) #the object in now robot_pos
    obj_metadata={} #get the object metadata
    result_json = {}
    robot_pose=robot.get_position()
    editable_states={object_states.Cooked:"cooked",object_states.Burnt:"burnt",object_states.Frozen:"frozen",object_states.Heated:"hot",
                     object_states.Open:"open",object_states.ToggledOn:"toggled_on",object_states.Folded:"folded",object_states.Unfolded:"unfolded"}
    for ele in sub_nowwehave:
        picpath=list(ele.keys())[0]
        objects=list(ele.values())[0]
        action=picpath.split("/")[-1][12:-4]
        scene_graph=parseSG(objects)
        if action not in actionlist:
            actionlist.append(action)
        obj_metadata.clear()
        for obj_name in objects:
            obj_metadata[obj_name]={}
            # ability=OBJECT_TAXONOMY.get_abilities(OBJECT_TAXONOMY.get_synset_from_category(obj_name.split("_")[0]))
            object=env.scene.object_registry("name",obj_name)
            states={"ability":[editable_states[sta] for sta in list(object.states.keys()) if sta in editable_states.keys()]}
            obj_metadata[obj_name].update(states)
            obj_in_rob=obj_in_robs[obj_name]
            position_in_bot={"position_in_bot":obj_in_rob[0]}
            result_json[action]={}
            obj_metadata[obj_name].update(position_in_bot)
            orientation={"orientation_in_bot":obj_in_rob[1].tolist()}
            obj_metadata[obj_name].update(orientation)
            position_in_world={"position_in_world":object.get_position().tolist()}
            obj_metadata[obj_name].update(position_in_world)
            bot_pose={"bot_in_world":robot_pose.tolist()}
            obj_metadata[obj_name].update(bot_pose)
            path={"path":picpath}
            obj_metadata[obj_name].update(path)
            for hextuple in seglists:
                if hextuple[0]==picpath:
                    if(obj_name==hextuple[1]):
                        bbox2d={"bbox2d":np.array(hextuple[4]).astype(float).tolist()}
                        obj_metadata[obj_name].update(bbox2d)
                        break
            result_json[action].update(obj_metadata)
            result_json[action].update(scene_graph)
        inventory_dict={"inventory":inventory}
        result_json[action].update(inventory_dict)
    return result_json

def writejson(FILENAME, result_json):
    with open(f"/shared/liushuai/OmniGibson/{FILENAME}/task.json","w")as f:
        json.dump(result_json,f)

def Update_camera_pos(camera, robot):
    pos = robot.get_position()
    cam_pos = get_camera_position(pos)
    camera.set_position(cam_pos)

def Update_camera_pos_bev(camera, robot):
    pos = robot.get_position()
    cam_pos = get_camera_position_bev(pos)
    camera.set_position(cam_pos)

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
