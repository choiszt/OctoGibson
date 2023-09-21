import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Turn on the stove to cook the bacon.
    stove = registry(env, "stove_rgpphy_0")
    toggle_on(robot, stove)
    donothing(env)
