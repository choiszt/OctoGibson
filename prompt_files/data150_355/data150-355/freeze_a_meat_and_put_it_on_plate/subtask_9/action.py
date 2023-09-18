import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the fridge is open, if not, open the fridge
    fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
    if fridge_dszchb_0['openable'] == 0:
        open(robot, fridge_dszchb_0)
        donothing(env)
