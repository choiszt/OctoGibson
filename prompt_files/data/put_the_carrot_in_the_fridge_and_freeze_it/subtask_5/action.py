import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the carrot inside the fridge
    carrot_177 = registry(env,"carrot_177")
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    put_inside(robot, carrot_177, fridge_xyejdx_0)
    donothing(env)
