import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Put the strawberry inside the fridge
    strawberry = registry(env, "strawberry_91")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, strawberry, fridge)
    donothing(env)
