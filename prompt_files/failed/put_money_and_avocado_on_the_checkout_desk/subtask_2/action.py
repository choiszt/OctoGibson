import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the money from the shopping cart.
    money = registry(env, "money_143")
    EasyGrasp(robot, money)
    donothing(env)
