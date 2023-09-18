import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the water bottle
    water_bottle = registry(env, "water_bottle_284")
    EasyGrasp(robot, water_bottle)
    donothing(env)
