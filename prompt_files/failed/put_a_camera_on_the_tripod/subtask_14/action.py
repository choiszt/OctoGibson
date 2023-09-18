import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the camera
    digital_camera_183 = registry(env,"digital_camera_183")
    EasyGrasp(robot, digital_camera_183)
    donothing(env)
