import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the cheese tart inside the fridge.
    cheese_tart_85 = registry(env, "cheese_tart_85")
    fridge_xyejdx_0 = registry(env, "fridge_xyejdx_0")
    put_inside(robot, cheese_tart_85, fridge_xyejdx_0)
    donothing(env)
