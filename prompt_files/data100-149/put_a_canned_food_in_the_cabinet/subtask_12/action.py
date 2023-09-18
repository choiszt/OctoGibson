import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the canned food
    canned_food_91 = registry(env,"canned_food_91")
    EasyGrasp(robot, canned_food_91)
    donothing(env)
