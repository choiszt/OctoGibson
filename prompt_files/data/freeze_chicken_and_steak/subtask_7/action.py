import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the steak in the fridge
    steak = registry(env, "steak_172")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, steak, fridge)
    donothing(env)
