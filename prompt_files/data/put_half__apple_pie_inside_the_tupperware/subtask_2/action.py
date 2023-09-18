import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the half apple pie
    half_apple_pie_189 = registry(env,"half_apple_pie_189")
    EasyGrasp(robot, half_apple_pie_189)
    donothing(env)
