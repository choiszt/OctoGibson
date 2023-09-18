import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the tupperware inside the fridge
    tupperware_91 = registry(env,"tupperware_91")
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    put_inside(robot, tupperware_91, fridge_xyejdx_0)
    donothing(env)
