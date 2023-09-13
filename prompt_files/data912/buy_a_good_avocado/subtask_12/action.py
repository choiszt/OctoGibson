import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the money.
    money_143 = registry(env,"money_143")
    EasyGrasp(robot, money_143)
    donothing(env)
