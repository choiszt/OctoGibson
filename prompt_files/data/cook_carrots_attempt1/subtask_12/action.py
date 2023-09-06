import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the stove object.
    stove = registry(env,"stove_rgpphy_0")
    # Subtask 2: Register the saucepot object.
    saucepot = registry(env,"saucepot_150")
    # Subtask 3: Move to the stove.
    MoveBot(env, robot, stove, camera)
    donothing(env)
