import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the tupperware inside the refrigerator
    tupperware_88 = registry(env,"tupperware_88")
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    put_inside(robot, tupperware_88, fridge_xyejdx_0)
    donothing(env)
