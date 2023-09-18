import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Cook the ham hocks in the stockpot
    stockpot = registry(env, "stockpot_81")
    cook(robot, stockpot)
    donothing(env)
