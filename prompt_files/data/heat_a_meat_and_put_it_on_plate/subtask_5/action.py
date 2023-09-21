import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take the meat out of the oven
    pork_chop = registry(env,"pork_chop_188")
    oven = registry(env,"oven_wuinhm_0")
    toggle_off(robot, oven)
    donothing(env)
    open(robot, oven)
    donothing(env)
    EasyGrasp(robot, pork_chop)
    donothing(env)
