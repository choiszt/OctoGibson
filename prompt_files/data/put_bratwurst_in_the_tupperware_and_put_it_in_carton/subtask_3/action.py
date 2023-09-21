import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the tupperware
    # Since the tupperware is not observed in the environment, we assume it's inside the opened bottom cabinet.
    # We need to wait for the system to capture the new state after opening the bottom cabinet.
    donothing(env)
