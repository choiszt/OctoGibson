import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the pickle from the fridge
    pickle = registry(env, "pickle_88")
    EasyGrasp(robot, pickle)
    donothing(env)
