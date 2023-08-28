import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    bacon = registry(env, "bacon_150")
    stove = registry(env, "stove_rgpphy_0")
    cook(robot, bacon)
    donothing(env)
    toggle_off(robot, stove)
    donothing(env)