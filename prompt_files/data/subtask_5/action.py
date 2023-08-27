import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    stove = registry(env, "stove_rgpphy_0")
    bacon = registry(env, "bacon_150")
    MoveBot(env, robot, stove, camera)
    donothing(env)
    toggle_on(robot, stove)
    donothing(env)