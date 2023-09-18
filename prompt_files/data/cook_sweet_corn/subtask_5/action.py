import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Heat the sweet corn in the stockpot
    stockpot = registry(env,"stockpot_155")
    heat(robot, stockpot)
    donothing(env)
