import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the ham hock
    ham_hock = registry(env, "ham_hock_82")
    EasyGrasp(robot, ham_hock)
    donothing(env)
