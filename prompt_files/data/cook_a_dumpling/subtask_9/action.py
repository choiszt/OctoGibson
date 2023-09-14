import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp a dumpling from the fridge
    dumpling = registry(env,"dumpling_153")
    EasyGrasp(robot, dumpling)
    donothing(env)
