import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the money
    money = registry(env, "money_145")
    EasyGrasp(robot, money)
    donothing(env)
