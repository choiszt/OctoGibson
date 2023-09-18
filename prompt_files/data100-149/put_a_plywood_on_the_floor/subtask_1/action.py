import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the plywood
    plywood_85 = registry(env,"plywood_85")
    EasyGrasp(robot, plywood_85)
    donothing(env)
