import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Register the pocketknife.
    pocketknife_278 = registry(env, "pocketknife_278")
    donothing(env)
