import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the spinach from the grocery shelf
    spinach = registry(env, "spinach_144")
    EasyGrasp(robot, spinach)
    donothing(env)
