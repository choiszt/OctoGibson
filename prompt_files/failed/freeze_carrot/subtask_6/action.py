import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the carrot in the fridge
    carrot = registry(env, "carrot_178")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, carrot, fridge)
    donothing(env)
