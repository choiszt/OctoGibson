import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the spinach
    spinach_189 = registry(env, "spinach_189")
    EasyGrasp(robot, spinach_189)
    donothing(env)
