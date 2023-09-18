import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the lettuce
    lettuce = registry(env, "lettuce_143")
    EasyGrasp(robot, lettuce)
    donothing(env)
