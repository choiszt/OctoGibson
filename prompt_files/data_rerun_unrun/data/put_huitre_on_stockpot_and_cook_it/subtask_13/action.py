import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the oyster on the countertop
    oyster = registry(env,"oyster_201")
    countertop = registry(env,"countertop_tpuwys_1")
    put_ontop(robot, oyster, countertop)
    donothing(env)
