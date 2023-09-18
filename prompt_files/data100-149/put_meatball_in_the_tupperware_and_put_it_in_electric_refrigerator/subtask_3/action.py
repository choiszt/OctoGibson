import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the tupperware from the bottom cabinet
    tupperware_194 = registry(env,"tupperware_194")
    EasyGrasp(robot, tupperware_194)
    donothing(env)
