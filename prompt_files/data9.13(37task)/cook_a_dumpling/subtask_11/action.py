import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the frying pan
    frying_pan = registry(env,"frying_pan_150")
    EasyGrasp(robot, frying_pan)
    donothing(env)
