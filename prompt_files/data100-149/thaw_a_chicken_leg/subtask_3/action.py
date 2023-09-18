import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Thaw the chicken thigh
    chicken_thigh = registry(env,"chicken_thigh_86")
    heat(robot, chicken_thigh)
    donothing(env)
