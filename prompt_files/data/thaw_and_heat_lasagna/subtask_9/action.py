import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Register the fridge
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    # Subtask 7: Open the fridge
    open(robot, fridge_xyejdx_0)
    donothing(env)
