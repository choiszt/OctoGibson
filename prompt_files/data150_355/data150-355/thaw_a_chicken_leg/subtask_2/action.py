import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the chicken thigh from the fridge
    chicken_thigh = registry(env,"chicken_thigh_86")
    EasyGrasp(robot, chicken_thigh)
    donothing(env)
