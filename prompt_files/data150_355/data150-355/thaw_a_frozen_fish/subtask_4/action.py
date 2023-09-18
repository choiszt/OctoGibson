import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the salmon on the countertop
    salmon = registry(env, "salmon_85")
    countertop = registry(env, "countertop_tpuwys_4")
    put_ontop(robot, salmon, countertop)
    donothing(env)
