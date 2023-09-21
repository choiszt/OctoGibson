import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the pottable marigold
    pottable_marigold_275 = registry(env, "pottable_marigold_275")
    EasyGrasp(robot, pottable_marigold_275)
    donothing(env)
