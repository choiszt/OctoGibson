import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the shrimp into the frying pan
    frying_pan = registry(env,"frying_pan_201")
    shrimp = registry(env,"shrimp_203")
    put_ontop(robot, shrimp, frying_pan)
    donothing(env)
