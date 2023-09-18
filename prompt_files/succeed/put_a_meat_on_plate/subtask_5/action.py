import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the pork chop on the plate
    pork_chop = registry(env, "pork_chop_188")
    plate = registry(env, "plate_190")
    put_ontop(robot, pork_chop, plate)
    donothing(env)
