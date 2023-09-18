import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Open the oven.
    oven = registry(env, "oven_wuinhm_0")
    open(robot, oven)
    donothing(env)
