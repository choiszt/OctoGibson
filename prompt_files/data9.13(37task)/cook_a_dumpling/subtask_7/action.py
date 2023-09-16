import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the dumpling into the frying pan
    dumpling = registry(env,"dumpling_154")
    frying_pan = registry(env,"frying_pan_150")
    put_ontop(robot, dumpling, frying_pan)
    donothing(env)
