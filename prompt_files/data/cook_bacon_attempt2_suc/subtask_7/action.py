import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Cook the bacon on the stove
    bacon = registry(env,"bacon_150")
    cook(robot, bacon)
    donothing(env)
