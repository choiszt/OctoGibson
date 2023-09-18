import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the pork chop and the plate
    pork_chop_188 = registry(env,"pork_chop_188")
    plate_190 = registry(env,"plate_190")
    
    # Subtask 2: Grasp the pork chop from the plate on the countertop
    EasyGrasp(robot, pork_chop_188)
    donothing(env)
    
    # Subtask 3: Put the pork chop back on the plate
    put_ontop(robot, pork_chop_188, plate_190)
    donothing(env)
