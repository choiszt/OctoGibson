import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Register the water bottle
    water_bottle_284 = registry(env,"water_bottle_284")
    # Subtask 5: Grasp the water bottle
    EasyGrasp(robot, water_bottle_284)
    donothing(env)
