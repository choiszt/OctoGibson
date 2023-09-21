import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the quail inside the fridge
    quail = registry(env,"quail")
    donothing(env)
