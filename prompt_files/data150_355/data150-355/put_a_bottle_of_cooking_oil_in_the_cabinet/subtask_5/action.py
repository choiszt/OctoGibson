import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the bottle_of_cooking_oil_88 inside the top_cabinet_dmwxyl_2
    bottle_of_cooking_oil_88 = registry(env,"bottle_of_cooking_oil_88")
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    put_inside(robot, bottle_of_cooking_oil_88, top_cabinet_dmwxyl_2)
    donothing(env)
