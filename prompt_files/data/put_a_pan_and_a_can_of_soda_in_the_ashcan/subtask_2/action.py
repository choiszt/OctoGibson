import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Search for the pan.
    # Since the pan is not observed in the environment, we need to search for it.
    # Here we assume the pan might be inside the notepad_86, so we will open it.
    notepad_86 = registry(env,"notepad_86")
    open(robot, notepad_86)
    donothing(env)
