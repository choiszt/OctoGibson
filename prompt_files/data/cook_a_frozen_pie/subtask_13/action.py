import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the cheese tart from the oven
    cheese_tart = registry(env,"cheese_tart_188")
    EasyGrasp(robot, cheese_tart)
    donothing(env)
