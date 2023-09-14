import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the strawberry inside the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    strawberry = registry(env, "strawberry_91")
    put_inside(robot, strawberry, fridge)
    donothing(env)
