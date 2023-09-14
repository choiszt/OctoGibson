import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the ham hocks into the stockpot
    ham_hocks = registry(env,"ham_hock_82")
    stockpot = registry(env,"stockpot_81")
    put_inside(robot, ham_hocks, stockpot)
    donothing(env)
