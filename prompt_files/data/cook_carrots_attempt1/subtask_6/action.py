import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the saucepot back onto the stove.
    stove = registry(env,"stove_rgpphy_0")
    saucepot = registry(env,"saucepot_150")
    put_ontop(robot, saucepot, stove)
    donothing(env)
