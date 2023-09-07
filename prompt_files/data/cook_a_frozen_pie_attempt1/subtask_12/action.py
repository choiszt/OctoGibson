import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Freeze the cheese tart
    cheese_tart = registry(env, "cheese_tart_188")
    freeze(robot, cheese_tart)
    donothing(env)
