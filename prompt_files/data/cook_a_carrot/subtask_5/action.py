import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Put the saucepot with the carrot onto the stove
    saucepot = registry(env,"saucepot_150")
    stove = registry(env,"stove_rgpphy_0")
    put_ontop(robot, saucepot, stove)
    donothing(env)
