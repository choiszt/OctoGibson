import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the tomato inside the refrigerator
    tomato = registry(env, "beefsteak_tomato_90")
    fridge = registry(env, "fridge_xyejdx_0")
    put_inside(robot, tomato, fridge)
    donothing(env)
