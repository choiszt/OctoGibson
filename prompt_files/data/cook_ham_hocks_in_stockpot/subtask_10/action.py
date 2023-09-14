import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the ham hock into the stockpot
    ham_hock = registry(env,"ham_hock_82")
    stockpot = registry(env,"stockpot_81")
    put_inside(robot, ham_hock, stockpot)
    donothing(env)
