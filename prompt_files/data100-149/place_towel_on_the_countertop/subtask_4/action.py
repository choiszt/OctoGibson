import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: If the towel is not inside the cabinet, search for it in the environment.
    # Since the towel is not inside the cabinet, we need to search for it in the environment.
    # However, the towel is not observed in the environment, so we cannot perform any actions in this step.
    donothing(env)
