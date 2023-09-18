import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the steak on the stove by heating the frying pan
    frying_pan = registry(env,"frying_pan_202")
    heat(robot, frying_pan)
    donothing(env)
