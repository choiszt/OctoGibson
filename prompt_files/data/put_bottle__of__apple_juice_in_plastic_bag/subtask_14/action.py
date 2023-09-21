import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle of apple juice
    bottle_of_apple_juice_146 = registry(env,"bottle_of_apple_juice_146")
    EasyGrasp(robot, bottle_of_apple_juice_146)
    donothing(env)
