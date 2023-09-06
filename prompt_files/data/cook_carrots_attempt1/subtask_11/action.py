import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the stove object.
    stove = registry(env,"stove_rgpphy_0")
    # Subtask 2: Check the state of the stove.
    if stove.togglable == 1:
        # Subtask 3: If the stove is on, toggle it off.
        toggle_off(robot, stove)
        donothing(env)
