import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the money from the checkout counter.
    money_143 = registry(env,"money_143")
    EasyGrasp(robot, money_143)
    donothing(env)
