import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take out the bacon from the fridge.
    bacon = registry(env, "bacon_150")
    EasyGrasp(robot, bacon)
    donothing(env)
