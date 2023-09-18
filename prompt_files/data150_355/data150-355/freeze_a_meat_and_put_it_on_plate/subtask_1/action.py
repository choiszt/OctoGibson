import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register all the objects
    pork_chop_188 = registry(env,"pork_chop_188")
    fridge_dszchb_0 = registry(env,"fridge_dszchb_0")
    plate_190 = registry(env,"plate_190")
    plate_191 = registry(env,"plate_191")
    # Subtask 2: Grasp the meat from the fridge
    EasyGrasp(robot, pork_chop_188)
    donothing(env)
