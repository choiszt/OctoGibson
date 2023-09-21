import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 10: Grasp the pear from the countertop
    pear_86 = registry(env,"pear_86")
    EasyGrasp(robot, pear_86)
    donothing(env)
