import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Freeze the pork chop
    pork_chop = registry(env, "pork_chop_188")
    freeze(robot, pork_chop)
    donothing(env)
