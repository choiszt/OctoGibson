import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the prawn
    shrimp_145 = registry(env,"shrimp_145")
    EasyGrasp(robot, shrimp_145)
    donothing(env)
