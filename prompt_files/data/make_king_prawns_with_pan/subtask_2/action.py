import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the shrimp out of the fridge
    shrimp = registry(env,"shrimp_203")
    EasyGrasp(robot, shrimp)
    donothing(env)
