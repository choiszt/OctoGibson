import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the mustard leaf from the countertop
    mustard_leaf_201 = registry(env,"mustard_leaf_201")
    EasyGrasp(robot, mustard_leaf_201)
    donothing(env)
