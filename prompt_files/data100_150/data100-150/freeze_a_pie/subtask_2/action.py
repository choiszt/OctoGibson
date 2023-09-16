import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Open the fridge.
    open(robot, fridge_xyejdx_0)
    donothing(env)
