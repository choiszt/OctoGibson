import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the oven
    oven_wuinhm_0 = registry(env,"oven_wuinhm_0")
    open(robot, oven_wuinhm_0)
    donothing(env)
