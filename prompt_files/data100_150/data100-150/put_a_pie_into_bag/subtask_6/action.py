import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the cheese_tart_280
    cheese_tart_280 = registry(env,"cheese_tart_280")
    EasyGrasp(robot, cheese_tart_280)
    donothing(env)
