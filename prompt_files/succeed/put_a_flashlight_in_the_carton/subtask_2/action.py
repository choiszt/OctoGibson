import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the flashlight
    flashlight = registry(env, "flashlight_192")
    EasyGrasp(robot, flashlight)
    donothing(env)
