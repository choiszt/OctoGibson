import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the tupperware
    tupperware = registry(env, "tupperware_193")
    EasyGrasp(robot, tupperware)
    donothing(env)
