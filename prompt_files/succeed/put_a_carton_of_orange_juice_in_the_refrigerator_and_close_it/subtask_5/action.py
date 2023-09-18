import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the carton of orange juice inside the refrigerator
    fridge_xyejdx_0 = registry(env,"fridge_xyejdx_0")
    carton_of_orange_juice_89 = registry(env,"carton_of_orange_juice_89")
    put_inside(robot, carton_of_orange_juice_89, fridge_xyejdx_0)
    donothing(env)
