import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the camera
    digital_camera_183 = registry(env,"digital_camera_183")
    MoveBot(env, robot, digital_camera_183, camera)
    donothing(env)
