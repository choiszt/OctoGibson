import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the fridge_xyejdx_0
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    open(robot, fridge_xyejdx_0)
    donothing(env)
