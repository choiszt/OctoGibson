import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Open the fridge to find the stockpot
    fridge = registry(env, "fridge_dszchb_0")
    open(robot, fridge)
    donothing(env)
