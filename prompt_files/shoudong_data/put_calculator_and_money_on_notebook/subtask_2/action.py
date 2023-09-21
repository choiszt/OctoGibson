import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the calculator from the grocery_shelf_prtqlw_1
    calculator_145 = registry(env, "calculator_145")
    EasyGrasp(robot, calculator_145)
    donothing(env)
