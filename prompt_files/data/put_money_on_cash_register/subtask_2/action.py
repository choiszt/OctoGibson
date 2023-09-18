import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 2: Grasp the money.
    money_146 = registry(env, "money_146")
    EasyGrasp(robot, money_146)
    donothing(env)
