import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the prawn from the fridge
    shrimp = registry(env,"shrimp_201")
    EasyGrasp(robot, shrimp)
    donothing(env)
