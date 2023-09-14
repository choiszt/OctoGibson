import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 10: Put down the peach
    peach = registry(env, "peach_173")
    countertop = registry(env, "countertop_tpuwys_1")
    put_ontop(robot, peach, countertop)
    donothing(env)
