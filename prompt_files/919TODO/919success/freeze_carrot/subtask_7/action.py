import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Toggle on the fridge_xyejdx_0 to freeze the carrot
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    toggle_on(robot, fridge_xyejdx_0)
    donothing(env)
