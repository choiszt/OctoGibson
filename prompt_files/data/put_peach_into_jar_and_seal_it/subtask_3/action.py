import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the peach from the fridge
    peach = registry(env, "peach_173")
    EasyGrasp(robot, peach)
    donothing(env)
