import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the ham hocks in the stockpot
    stockpot = registry(env, "stockpot_81")
    ham_hocks = registry(env, "ham_hock_82")
    put_ontop(robot, ham_hocks, stockpot)
    donothing(env)
