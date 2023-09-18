import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Register the prawn
    shrimp_201 = registry(env, "shrimp_201")
    # Subtask 9: Cook the prawn
    cook(robot, shrimp_201)
    donothing(env)
