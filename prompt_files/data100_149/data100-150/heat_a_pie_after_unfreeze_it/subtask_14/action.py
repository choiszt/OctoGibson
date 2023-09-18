import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Heat the cheese tart to unfreeze it
    cheese_tart = registry(env, "cheese_tart_188")
    heat(robot, cheese_tart)
    donothing(env)
