import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the fries
    french_fries = registry(env, "french_fries_88")
    heat(robot, french_fries)
    donothing(env)
