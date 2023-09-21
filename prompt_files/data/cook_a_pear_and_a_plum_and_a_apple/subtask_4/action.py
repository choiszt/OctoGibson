import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the pear on the countertop
    pear_86 = registry(env,"pear_86")
    countertop_tpuwys_2 = registry(env,"countertop_tpuwys_2")
    put_ontop(robot, pear_86, countertop_tpuwys_2)
    donothing(env)
