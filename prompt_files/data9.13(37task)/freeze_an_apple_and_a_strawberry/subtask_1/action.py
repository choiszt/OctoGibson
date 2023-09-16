import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register all the objects needed
    fridge = registry(env, "fridge_xyejdx_0")
    # Subtask 2: Open the fridge
    open(robot, fridge)
    donothing(env)
