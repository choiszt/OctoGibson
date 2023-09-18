import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the frying pan with the steak on the stove
    frying_pan = registry(env,"frying_pan_202")
    stove = registry(env,"stove_igwqpj_0")
    put_ontop(robot, frying_pan, stove)
    donothing(env)
