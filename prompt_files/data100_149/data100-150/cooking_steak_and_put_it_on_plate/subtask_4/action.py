import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the steak on the frying pan
    frying_pan = registry(env,"frying_pan_202")
    steak = registry(env,"steak_201")
    put_ontop(robot, steak, frying_pan)
    donothing(env)
