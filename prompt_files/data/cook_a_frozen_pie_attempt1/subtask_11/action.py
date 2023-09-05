import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the cheese tart inside the fridge to freeze it
    cheese_tart = registry(env, "cheese_tart_188")
    fridge = registry(env, "fridge_dszchb_0")
    put_inside(robot, cheese_tart, fridge)
    donothing(env)
