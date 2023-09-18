import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the fridge is open, if not, open the fridge
    fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
    observed_objects = env.get_observed_objects()
    for obj in observed_objects:
        if obj[0] == 'fridge_dszchb_0':
            if ('openable', 0) in obj[1]:
                open(robot, fridge_dszchb_0)
                donothing(env)
                break
