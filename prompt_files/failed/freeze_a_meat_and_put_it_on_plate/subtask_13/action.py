import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Freeze the meat
    pork_chop_188 = registry(env,"pork_chop_188")
    freeze(robot, pork_chop_188)
    donothing(env)
