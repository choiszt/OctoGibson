import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the chicken from the fridge
    chicken = registry(env,"chicken_189")
    EasyGrasp(robot, chicken)
    donothing(env)
