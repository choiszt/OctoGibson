import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the money from the shopping_cart_kmgltg_1
    money_149 = registry(env, "money_149")
    EasyGrasp(robot, money_149)
    donothing(env)
