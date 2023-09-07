import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: If the stove is on, toggle it off.
    stove = registry(env,"stove_rgpphy_0")
    if stove['togglable'] == 1:
        toggle_off(robot, stove)
        donothing(env)
