import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the cheese tart into the oven
    fridge = registry(env, "fridge_dszchb_0")
    open(robot, fridge)
    donothing(env)
