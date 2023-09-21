import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Register the fridge
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
