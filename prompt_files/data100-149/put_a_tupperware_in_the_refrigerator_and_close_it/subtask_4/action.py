import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the tupperware
    tupperware_88 = registry(env,"tupperware_88")
    EasyGrasp(robot, tupperware_88)
    donothing(env)
