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
class ROBOT():
    def __init__(self,robot,env):
        self.robot=robot
        self.env=env
    def EasyGrasp(self, obj, dis_threshold):
        #Grasp the robot within the distance threshold
        robot_pos = self.robot.get_position()
        obj_pose = obj.get_position()
        dis = cal_dis(robot_pos, obj_pose)
        # if dis < dis_threshold:
        robot_pos[2] += self.robot.aabb_center[2]
        robot_pos[2] -=0.2
        obj.set_position(robot_pos)
        if len(self.robot.inventory)>1:
            raise Exception("robot carries more than 1 object!")
        self.robot.inventory.append(obj._name)
        print(f"now we have:{self.robot.inventory}")
    #     return True
    # else:
    #     return False

    def Hold(self, obj_name):
        # Hold the objects
        robot_pos = self.robot.get_position()
        robot_pos[2] += self.robot.aabb_center[2]
        robot_pos[2] -=0.2
        obj=self.env.scene.object_registry("name",obj_name)  
        obj.set_position(robot_pos)

    def MoveBot(self, obj):
        self.robot.set_position(obj)
        if self.robot.inventory:
            # relationship between name and variable.
            obj = self.robot.inventory[0]
            self.Hold(obj)
    
    def EasyDrop(self,obj, pos, dis_threshold): #TODO possible function  EasyDrop_V2(robot,obj1, obj2, dis_threshold) (put the OBJ1 <predicate> OBJ2)
        # Drop the objects within robot's hands
        obj_pos = obj.get_position()
        dis = cal_dis(obj_pos, pos)
        obj.set_position(pos)
        if dis < dis_threshold:
            obj.set_position(pos)
            a=self.robot.inventory.pop()        
            print(f"the robot throw {a},now we have:{self.robot.inventory}")
        #     return True
        # else:
        #     return False

# def Teleport(robot, obj, pos):
#     # Teleport the robot and the objects within its hands
#     robot.set_position(pos)
#     Hold(robot, obj)





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
    def __init__(self,robot,camera,env,filename,position=np.array([-2.48302418,  1.55655398,  2.22882511]),orientation=np.array([ 0.56621324, -0.0712958 , -0.10258276,  0.81473692])):
        self.robot=robot
        self.camera=camera
        self.env=env
        self.camera.set_position_orientation(
        position=position,
        orientation=orientation)
        self.seglist=[]  #(seg_file_id,object_name,objectclass,instance_id,2d_bbox,3d_bbox)
        self.instancemap=[]
        self.FILENAME=filename
        self.allobject=self._getallobject()
        self.result_json={}
        self.actionlist=[] #check the action to appear only once
    def _getallobject(self):
        allobject=[]
        try:
            objectlist=[i['name'] for i in self.env.objects_config]
        except:
            pass
        scenedict=self.env.scene.get_objects_info()
        scenelist=list(scenedict['init_info'].keys())
        return list(set(objectlist+scenelist))
    def setposition(self,position=None,orientation=None):
        if type(orientation)==np.ndarray and type(position)!=np.ndarray:
            self.camera.set_orientation(orientation)
        if type(orientation)!=np.ndarray and type(position)==np.ndarray:
            self.camera.set_position(position)
        if  type(orientation)==np.ndarray and type(position)==np.ndarray:
            self.camera.set_position_orientation(position=position,orientation=orientation)
        else:
            raise TypeError
        
    def xyz2spherical(self,position):
        x,y,z=[position[i] for i in range(3)]
        rho=math.sqrt(x**2+y**2+z**2)
        theta=math.atan2(y,x)
        phi=math.acos(z/rho)

        #convert to degree
        theta_deg=math.degrees(theta)
        phi_deg=math.degrees(phi)
        return {"rho":rho,"theta_deg":theta_deg,"phi_deg":phi_deg}

    def set_in_rob(self,robot):
        obj_in_rob={}
        for object_name in self.allobject:
            tempobj=self.env.scene.object_registry("name",object_name)
            pose_in_rob=self.align_coord(tempobj,robot)
            obj_in_rob[object_name]=(self.xyz2spherical(pose_in_rob[0]),pose_in_rob[1])
        return obj_in_rob
                
    def align_coord(self,obj,rob):
        #choiszt convert world2bot coord
        obj_in_world = T.pose2mat(obj.get_position_orientation())
        rob_in_world = T.pose2mat(rob.get_position_orientation())
        world_in_rob = T.pose_inv(rob_in_world)
        #same with T.relative_pose_transform(tempobj.get_position(),tempobj.get_orientation(),robot.get_position(),robot.get_orientation()) ## choiszt have varified this 
        obj_in_rob = T.pose_in_A_to_pose_in_B(obj_in_world, world_in_rob)
        obj2rob =T.mat2pose(obj_in_rob)
        return obj2rob

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
                    self.instancemap.append({f"/shared/liushuai/OmniGibson/{self.FILENAME}/"+query_name + f'{iter}.png':obs_dict[query_name][0]})
                    segimg = segmentation_to_rgb(obs_dict[query_name][0], N=256)
                    instancemap = obs_dict[query_name][1]
                    for item in instancemap:
                        bbox_3ds=obs_dict['bbox_3d']
                        bbox_2ds=obs_dict["bbox_2d_loose"] #
                        hextuple=[f"/shared/liushuai/OmniGibson/{self.FILENAME}/"+query_name + f'{iter}.png',item[1].split("/")[-1],item[3],item[0],'','']
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
                        self.seglist.append(hextuple)
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
                    cv2.imwrite(f"/shared/liushuai/OmniGibson/{self.FILENAME}/"+query_name + f'{iter}.png', rgbimg)
                    print(f"save as:{query_name + f'{iter}.png'}")
        
    def parsing_segmentdata(self): #parse all data from the files that we have collected
        seglists=self.seglist
        instancemaps=self.instancemap
        parse=lambda path:list(path.keys())[0]
        self.nowwehave=[]
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
            self.nowwehave.append(tempdict) #dict{path:object_name}
        print("now begin to parse segmentation data")
        return self.nowwehave
    
    def parseSG(self,objects):
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
            obj0=self.env.scene.object_registry("name",pair[0])
            obj1=self.env.scene.object_registry("name",pair[1])
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

    def collectdata_v2(self,robot): #each time change the robot position need to collectdata
        nowwehave=self.parsing_segmentdata()
        inventory=self.robot.inventory
        sub_nowwehave=[]
        for key in nowwehave:
            if list(key.keys())[0].split("/")[-1].rstrip('.png').lstrip("seg_instance") not in self.actionlist:
                sub_nowwehave.append(key)
        seglists=self.seglist
        obj_in_robs=self.set_in_rob(robot) #the object in now robot_pos
        obj_metadata={} #get the object metadata
        robot_pose=robot.get_position()
        editable_states={object_states.Cooked:"cooked",object_states.Burnt:"burnt",object_states.Frozen:"frozen",object_states.Heated:"hot",
                         object_states.Open:"open",object_states.ToggledOn:"toggled_on",object_states.Folded:"folded",object_states.Unfolded:"unfolded"}

        for ele in sub_nowwehave:
            picpath=list(ele.keys())[0]
            objects=list(ele.values())[0]
            action=picpath.split("/")[-1][12:-4]
            scene_graph=self.parseSG(objects)
            if action not in self.actionlist:
                self.actionlist.append(action)
            obj_metadata.clear()
            for obj_name in objects:
                obj_metadata[obj_name]={}
                # ability=OBJECT_TAXONOMY.get_abilities(OBJECT_TAXONOMY.get_synset_from_category(obj_name.split("_")[0]))
                object=self.env.scene.object_registry("name",obj_name)
                states={"ability":[editable_states[sta] for sta in list(object.states.keys()) if sta in editable_states.keys()]}
                obj_metadata[obj_name].update(states)


                obj_in_rob=obj_in_robs[obj_name]
                position_in_bot={"position_in_bot":obj_in_rob[0]}
                self.result_json[action]={}
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
                self.result_json[action].update(obj_metadata)
                self.result_json[action].update(scene_graph)
            inventory_dict={"inventory":inventory}
            self.result_json[action].update(inventory_dict)
        return self.result_json

    def writejson(self):
        with open(f"/shared/liushuai/OmniGibson/{self.FILENAME}/task.json","w")as f:
            json.dump(self.result_json,f)

    def collectdata(self):
        seglists=self.seglist
        result_json={}
        obj_metadata={} #get the object metadata
        for ele in self.nowwehave:
            picpath=list(ele.keys())[0]
            objects=list(ele.values())[0]
            action=picpath.split("/")[-1].rstrip('.png').lstrip("seg_instance")
            # result_json.clear()
            obj_metadata.clear()
            for obj_name in objects:
                object=self.env.scene.object_registry("name",obj_name)
                position={"position":object.get_position().tolist()}
                result_json[action]={}
                obj_metadata[obj_name]={}
                obj_metadata[obj_name].update(position)
                orientation={"orientation":object.get_orientation().tolist()}
                obj_metadata[obj_name].update(orientation)
                path={"path":picpath}
                obj_metadata[obj_name].update(path)
                for hextuple in seglists:
                    if hextuple[0]==picpath:
                        if(obj_name==hextuple[1]):
                            bbox2d={"bbox2d":np.array(hextuple[4]).astype(float).tolist()}
                            bbox3d={"bbox3d":np.array(hextuple[5][0:6]).astype(float).tolist(),"transform":hextuple[5][6].tolist(),"corners":hextuple[5][7].tolist()}
                            obj_metadata[obj_name].update(bbox2d)
                            obj_metadata[obj_name].update(bbox3d)
                            break
                result_json[action].update(obj_metadata)
        with open(f"/shared/liushuai/OmniGibson/{self.FILENAME}/task.json","w")as f:
            json.dump(result_json,f)
        return result_json



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

from collections import OrderedDict
def donothing(env, navi):
    dumbact=OrderedDict([('robot0', navi)])
    step=0
    for _ in range(30):
        # og.sim.step()
        env.step(dumbact)
        step += 1

from scipy.spatial.transform import Rotation as R
def trans_camera(q):
    random_yaw = np.pi / 2
    yaw_orn = R.from_euler("Z", random_yaw)
    new_camera_orn = quaternion_multiply(yaw_orn.as_quat(), q)
    print(new_camera_orn)
    return new_camera_orn

def change_states(obj, states, oper):
    '''
    obj (Objects): The object that the states are needed to be changed.
    states (str): The specific states to be changed.
    oper (int): 0 or 1, meaning the False or True of the states.
    '''

    # TODO: get the states we can edit @Choizst
    # TODO: translate the states to class, for example: open
    all_states = []
    black_list = [] # the states that cannot be set to True or False

    assert states in all_states and states not in black_list

    obj.states[CLASS(states)].set_value(oper)