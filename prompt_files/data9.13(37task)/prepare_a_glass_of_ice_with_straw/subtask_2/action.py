import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out an ice cube from the fridge
    ice_cube = registry(env, "ice_cube_87")
    EasyGrasp(robot, ice_cube)
    donothing(env)
