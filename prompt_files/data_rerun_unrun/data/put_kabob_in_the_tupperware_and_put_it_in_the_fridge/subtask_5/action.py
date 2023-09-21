import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the tupperware
    tupperware_91 = registry(env,"tupperware_91")
    EasyGrasp(robot, tupperware_91)
    donothing(env)
