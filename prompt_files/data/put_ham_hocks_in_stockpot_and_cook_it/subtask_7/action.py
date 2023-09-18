import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the stockpot
    stockpot = registry(env, "stockpot_81")
    EasyGrasp(robot, stockpot)
    donothing(env)
