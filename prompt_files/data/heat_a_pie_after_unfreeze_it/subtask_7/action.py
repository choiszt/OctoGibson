import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the pie in the oven
    oven = registry(env, "oven_wuinhm_0")
    cheese_tart = registry(env, "cheese_tart_188")
    put_inside(robot, cheese_tart, oven)
    donothing(env)
