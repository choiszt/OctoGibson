import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Take the cheese tart out of the oven
    cheese_tart = registry(env, "cheese_tart_188")
    oven = registry(env, "oven_wuinhm_0")
    EasyGrasp(robot, cheese_tart)
    donothing(env)
