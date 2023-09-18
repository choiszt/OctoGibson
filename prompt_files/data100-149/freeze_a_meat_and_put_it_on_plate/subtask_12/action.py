import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the meat in the fridge
    pork_chop_188 = registry(env,"pork_chop_188")
    fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
    put_inside(robot, pork_chop_188, fridge_dszchb_0)
    donothing(env)
