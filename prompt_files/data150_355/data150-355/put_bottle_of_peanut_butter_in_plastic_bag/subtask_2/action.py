import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle of peanut butter.
    bottle_of_peanut_butter_148 = registry(env,"bottle_of_peanut_butter_148")
    EasyGrasp(robot, bottle_of_peanut_butter_148)
    donothing(env)
