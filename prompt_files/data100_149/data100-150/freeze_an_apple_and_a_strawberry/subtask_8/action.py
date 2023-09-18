import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the apple inside the fridge
    apple = registry(env, "apple_88")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, apple, fridge)
    donothing(env)
