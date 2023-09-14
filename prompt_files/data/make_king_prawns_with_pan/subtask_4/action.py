import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Cook the shrimp
    shrimp = registry(env,"shrimp_203")
    cook(robot, shrimp)
    donothing(env)
