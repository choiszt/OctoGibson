import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put down jar_171
    jar = registry(env, "jar_171")
    countertop = registry(env, "countertop_tpuwys_1")
    put_ontop(robot, jar, countertop)
    donothing(env)
