import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the tablefork and the dishwasher
    tablefork_196 = registry(env,"tablefork_196")
    dishwasher_znfvmj_0 = registry(env,"dishwasher_znfvmj_0")
    
    # Subtask 2: Grasp the tablefork
    EasyGrasp(robot, tablefork_196)
    donothing(env)
