import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find and move to a stockpot
    stockpot = registry(env, "stockpot_123") # Assume the stockpot's name is stockpot_123
    MoveBot(env, robot, stockpot, camera)
    donothing(env)
