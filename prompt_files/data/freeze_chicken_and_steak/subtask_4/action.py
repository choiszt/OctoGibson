import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the chicken in the fridge
    chicken = registry(env, "chicken_176")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, chicken, fridge)
    donothing(env)
