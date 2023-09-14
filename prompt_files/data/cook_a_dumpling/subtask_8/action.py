import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Cook the dumpling
    dumpling = registry(env,"dumpling_154")
    cook(robot, dumpling)
    donothing(env)
