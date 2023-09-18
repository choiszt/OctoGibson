import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the tupperware from the bottom cabinet.
    tupperware = registry(env,"tupperware_1234") # assuming the tupperware is named "tupperware_1234"
    EasyGrasp(robot, tupperware)
    donothing(env)
