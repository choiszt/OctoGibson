import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Open the fridge
    fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
    open(robot, fridge_dszchb_0)
    donothing(env)
