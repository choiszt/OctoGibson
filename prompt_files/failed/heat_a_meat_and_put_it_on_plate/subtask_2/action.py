import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the pork chop from the fridge
    pork_chop = registry(env, "pork_chop_188")
    EasyGrasp(robot, pork_chop)
    donothing(env)
