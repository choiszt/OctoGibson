import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the pie out of the fridge
    cheese_tart = registry(env, "cheese_tart_188")
    EasyGrasp(robot, cheese_tart)
    donothing(env)
