#4 bev+1ego
import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import KeyboardRobotController
from omnigibson.sensors import VisionSensor
from omnigibson import object_states
import numpy as np
import json
import robot_action as ra
#ADD "--/log/level=error --/log/fileLogLevel=error --/log/outputStreamLevel=error"
# Configure macros for maximum performance
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True
gm.ENABLE_OBJECT_STATES = True
gm.ENABLE_TRANSITION_RULES = False
from robot_action import *
import yaml

def main(random_selection=False, headless=False, short_exec=False):

    config_filename="/shared/liushuai/OmniGibson/project/bddl_demo.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)
    cfg["task"]["online_object_sampling"] = False
    # Load the environment
    env = og.Environment(configs=cfg)

    robot=ROBOT(env.robots[0],env)

    robot.robot.set_position([-1.53887291 ,4.79978561 ,0.01504258])
    
    action_generator = KeyboardRobotController(robot=robot.robot)
    for sensor in robot.robot.sensors.values():
        if isinstance(sensor, VisionSensor):
            sensor.image_height = 720
            sensor.image_width = 720
    # Print out relevant keyboard info if using keyboard teleop
    action_generator.print_keyboard_teleop_info()   

    camera= og.sim.viewer_camera 
    bbox_modalities = ["bbox_3d", "bbox_2d_loose"]# "bbox_2d_tight" not use 
    for bbox_modality in bbox_modalities:
        camera.add_modality(bbox_modality)
    camera.focal_length = 10.
    cam=Camera(robot=env.robots[0],camera=camera,env=env,filename="trash") #initiated camera

    max_steps = -1 if not short_exec else 100    
    step=0
    iter=0
    while step != max_steps:

        action=np.zeros(11)
        ppposition=robot.robot.get_position()
        cam_position=ra.get_camera_position(ppposition)
        robot_sensor = robot.robot._sensors['robot0:eyes_Camera_sensor']
        rs_p, rs_o = robot_sensor.get_position_orientation()
        cam.setposition(cam_position, rs_o)

        donothing(env, action)
        print("ego:detect surroundings!!")
        for i in range(4):
            cam.FlyingCapture(f'{iter}_detect_surroundings')   
            iter+=1   

            Turn_90(robot.robot)
            rs_o = ra.trans_camera(rs_o)
            cam.setposition(cam_position, rs_o)

            donothing(env, action) 
        
        cam.collectdata_v2(robot.robot)
        donothing(env, action)


        cam.writejson()


    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()