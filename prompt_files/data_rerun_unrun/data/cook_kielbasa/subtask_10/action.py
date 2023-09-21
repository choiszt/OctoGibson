import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the kielbasa inside the fridge
    kielbasa = registry(env, "kielbasa")
    donothing(env)
