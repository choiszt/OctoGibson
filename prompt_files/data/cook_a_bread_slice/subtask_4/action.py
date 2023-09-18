import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Turn on the toaster
    toaster = registry(env, "toaster_85")
    toggle_on(robot, toaster)
    donothing(env)
