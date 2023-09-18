import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Check if the towel is inside the cabinet
    # Since the towel is not inside the cabinet, no action is needed in this step.
    donothing(env)
