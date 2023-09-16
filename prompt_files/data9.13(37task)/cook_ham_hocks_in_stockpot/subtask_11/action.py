import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the stockpot onto the oven
    oven = registry(env,"oven_wuinhm_0")
    stockpot = registry(env,"stockpot_81")
    put_ontop(robot, stockpot, oven)
    donothing(env)
