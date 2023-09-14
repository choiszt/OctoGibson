import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the ham hock in the stockpot
    ham_hock = registry(env,"ham_hock_82")
    stockpot = registry(env,"stockpot_81")
    cook(robot, ham_hock)
    donothing(env)
