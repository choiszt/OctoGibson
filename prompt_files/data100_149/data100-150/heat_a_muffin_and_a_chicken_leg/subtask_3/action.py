import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out a chicken leg from the fridge
    chicken_leg = registry(env,"chicken_thigh_86")
    EasyGrasp(robot, chicken_leg)
    donothing(env)
