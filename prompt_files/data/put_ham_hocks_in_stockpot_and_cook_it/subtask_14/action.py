import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the ham hocks inside the stockpot
    ham_hock_82 = registry(env,"ham_hock_82")
    stockpot_81 = registry(env,"stockpot_81")
    put_inside(robot, ham_hock_82, stockpot_81)
    donothing(env)
