import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Cook the bacon
    bacon = registry(env, "bacon_150")
    cook(robot, bacon)
    donothing(env)
