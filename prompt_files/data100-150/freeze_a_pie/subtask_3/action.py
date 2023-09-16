import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Register the fridge and open it.
    fridge_xyejdx_0 = registry(env, "fridge_xyejdx_0")
    open(robot, fridge_xyejdx_0)
    donothing(env)
