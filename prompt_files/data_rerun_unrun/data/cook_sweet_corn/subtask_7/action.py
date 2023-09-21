import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the stockpot on the stove
    stockpot = registry(env,"stockpot_155")
    stove = registry(env,"stove_rgpphy_0")
    put_ontop(robot, stockpot, stove)
    donothing(env)
