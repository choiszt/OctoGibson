import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the strawberries from the fridge
    strawberries = registry(env, "strawberries_86")
    EasyGrasp(robot, strawberries)
    donothing(env)
