import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the stockpot
    stockpot = registry(env, "stockpot_123")
    EasyGrasp(robot, stockpot)
    donothing(env)
