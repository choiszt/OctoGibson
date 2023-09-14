import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Cook the dumpling
    frying_pan = registry(env,"frying_pan_150")
    cook(robot, frying_pan)
    donothing(env)
