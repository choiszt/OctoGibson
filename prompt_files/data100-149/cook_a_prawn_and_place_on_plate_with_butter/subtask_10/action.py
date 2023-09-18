import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Cook the prawn
    cook(robot, shrimp)
    donothing(env)
