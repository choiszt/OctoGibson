import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle_of_cooking_oil_88
    bottle_of_cooking_oil_88 = registry(env,"bottle_of_cooking_oil_88")
    EasyGrasp(robot, bottle_of_cooking_oil_88)
    donothing(env)
