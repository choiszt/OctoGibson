import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the pan and the can of soda.
    pan = registry(env, "pan")
    can_of_soda = registry(env, "can_of_soda")
