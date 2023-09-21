import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the chicken inside the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    chicken = registry(env, "chicken_176")
    put_inside(robot, chicken, fridge)
    donothing(env)
