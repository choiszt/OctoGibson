import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the fruitcake inside the oven
    oven_wuinhm_0 = registry(env,"oven_wuinhm_0")
    fruitcake_188 = registry(env,"fruitcake_188")
    put_inside(robot, fruitcake_188, oven_wuinhm_0)
    donothing(env)
