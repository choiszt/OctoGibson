import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Heat the stockpot in the oven
    stockpot = registry(env, "stockpot_81")
    heat(robot, stockpot)
    donothing(env)
