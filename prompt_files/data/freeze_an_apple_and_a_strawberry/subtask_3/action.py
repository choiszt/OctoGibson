import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the apple inside the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    apple = registry(env, "apple_88")
    put_inside(robot, apple, fridge)
    donothing(env)
