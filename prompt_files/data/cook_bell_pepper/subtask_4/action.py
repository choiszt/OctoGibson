import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the bell pepper.
    # Since the bell pepper is not observed in the environment, we need to open the fridge to find it.
    fridge = registry(env, "fridge_1234")
    open(robot, fridge)
    donothing(env)
