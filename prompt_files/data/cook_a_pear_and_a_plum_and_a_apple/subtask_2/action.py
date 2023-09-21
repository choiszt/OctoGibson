import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Cook the pear
    pear_86 = registry(env,"pear_86")
    cook(robot, pear_86)
    donothing(env)
