import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Turn on the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    toggle_on(robot, fridge)
    donothing(env)
