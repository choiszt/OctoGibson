import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the dishwasher
    dishwasher = registry(env, "dishwasher_dngvvi_0")
    open(robot, dishwasher)
    donothing(env)
