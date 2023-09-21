import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the ham hocks in the stockpot
    stockpot = registry(env, "stockpot_81")
    ham_hock = registry(env, "ham_hock_82")
    put_ontop(robot, ham_hock, stockpot)
    donothing(env)
