import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the carton of milk inside the fridge
    fridge = registry(env,"fridge_xyejdx_0")
    carton_of_milk = registry(env,"carton_of_milk_86")
    put_inside(robot, carton_of_milk, fridge)
    donothing(env)
