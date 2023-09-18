import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the backpack
    backpack = registry(env, "backpack_88")
    EasyGrasp(robot, backpack)
    donothing(env)
