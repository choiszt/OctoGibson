import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the baseball
    baseball_88 = registry(env,"baseball_88")
    EasyGrasp(robot, baseball_88)
    donothing(env)
