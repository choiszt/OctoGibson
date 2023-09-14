import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the ham hock out of the fridge
    ham_hock = registry(env,"ham_hock_82")
    fridge = registry(env,"fridge_xyejdx_0")
    EasyGrasp(robot, ham_hock)
    donothing(env)
