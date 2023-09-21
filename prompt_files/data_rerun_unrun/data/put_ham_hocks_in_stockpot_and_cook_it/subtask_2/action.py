import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the ham hocks from the fridge
    ham_hock = registry(env, "ham_hock_82")
    EasyGrasp(robot, ham_hock)
    donothing(env)
