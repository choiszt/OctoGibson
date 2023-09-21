import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Turn on the oven
    oven = registry(env, "oven_wuinhm_0")
    toggle_on(robot, oven)
    donothing(env)
