import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the cheese tart
    cheese_tart = registry(env, "cheese_tart_188")
    cook(robot, cheese_tart)
    donothing(env)
