import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the carboy
    carboy = registry(env, "reagent_bottle_189")
    EasyGrasp(robot, carboy)
    donothing(env)
