import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the mustard leaf into the saucepan
    saucepan_205 = registry(env,"saucepan_205")
    mustard_leaf_201 = registry(env,"mustard_leaf_201")
    put_inside(robot, mustard_leaf_201, saucepan_205)
    donothing(env)
