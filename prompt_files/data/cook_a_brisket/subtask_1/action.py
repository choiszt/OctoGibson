import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Registration
    fridge = registry(env, "fridge_dszchb_0")
    # Subtask 1: Open the fridge
    open(robot, fridge)
    donothing(env)
