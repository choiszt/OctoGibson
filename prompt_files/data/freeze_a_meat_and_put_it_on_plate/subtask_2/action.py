import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the pork chop out of the fridge
    pork_chop = registry(env, "pork_chop_188")
    open(robot, "fridge_dszchb_0")
    donothing(env)
    EasyGrasp(robot, pork_chop)
    donothing(env)
