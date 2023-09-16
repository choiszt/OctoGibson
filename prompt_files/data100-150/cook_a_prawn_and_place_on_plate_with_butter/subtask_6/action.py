import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the prawn on the stove
    shrimp = registry(env,"shrimp_201")
    cook(robot, shrimp)
    donothing(env)
