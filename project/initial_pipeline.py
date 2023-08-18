#4 bev+1ego
import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import KeyboardRobotController
from omnigibson.sensors import VisionSensor
from omnigibson import object_states
import numpy as np
import json
#ADD "--/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error"
# Configure macros for maximum performance
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = True
gm.ENABLE_TRANSITION_RULES = False
from robot_action import *
import yaml

def init_pipeline(env, robot, camera, random_selection=False, headless=False, short_exec=False, file_name=None):
    iter=0
    cam=Camera(robot=env.robots[0],camera=camera,env=env,filename="818_test_gpt")
    robot=ROBOT(env.robots[0],env)

    robot.robot.visible=False
    
    action=np.zeros(11)
    ppposition=robot.robot.get_position()
    cam_position=get_camera_position(ppposition)
    robot_sensor = robot.robot._sensors['robot0:eyes_Camera_sensor']
    rs_p, rs_o = robot_sensor.get_position_orientation()
    cam.setposition(cam_position, rs_o)
    
    donothing(env, action)
    print("ego:detect surroundings!!")
    for i in range(4):
        cam.FlyingCapture(f'{iter}_detect_surroundings')   
        iter+=1   
        Turn_90(robot.robot)
        rs_o = trans_camera(rs_o)
        cam.setposition(cam_position, rs_o)
        donothing(env, action) 
    
    cam.collectdata_v2(robot.robot)
    
    donothing(env, action)
    robot.robot.visible=True
    robot.robot.set_position([-1.53887291 ,4.79978561 ,0.01504258])
    ppposition=robot.robot.get_position()
    cam_position=get_camera_position_bev(ppposition)
    cam.setposition(cam_position, trans_camera(robot.robot.get_orientation()))
    donothing(env, action)
    cam.FlyingCapture(f'{iter}_BEV_surroundings')   
    iter+=1  

    donothing(env, action)
    cam.collectdata_v2(robot.robot)
    jsonpath=cam.writejson()
    return jsonpath