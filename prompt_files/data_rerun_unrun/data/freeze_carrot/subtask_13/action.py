import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the carrot inside the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    carrot = registry(env, "carrot_178")
    put_inside(robot, carrot, fridge)
    donothing(env)
