import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the oyster on the stockpot
    # Assuming the stockpot is on the countertop
    stockpot = registry(env,"countertop_tpuwys_1")
    oyster = registry(env,"oyster_201")
    put_ontop(robot, oyster, stockpot)
    donothing(env)
