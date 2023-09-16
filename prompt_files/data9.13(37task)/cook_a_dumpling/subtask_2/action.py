import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the tupperware from the fridge
    tupperware = registry(env,"tupperware_156")
    EasyGrasp(robot, tupperware)
    donothing(env)
