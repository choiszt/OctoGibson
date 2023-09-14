import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Freeze the steak
    steak = registry(env, "steak_172")
    freeze(robot, steak)
    donothing(env)
