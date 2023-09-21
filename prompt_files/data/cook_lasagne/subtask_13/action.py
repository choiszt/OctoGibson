import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Turn off the oven
    oven_wuinhm_0 = registry(env,"oven_wuinhm_0")
    toggle_off(robot,oven_wuinhm_0)
    donothing(env)
