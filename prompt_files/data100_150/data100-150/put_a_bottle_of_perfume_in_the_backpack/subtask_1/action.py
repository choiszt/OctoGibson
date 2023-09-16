import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the bottle of perfume and the backpack
    bottle_of_perfume_85 = registry(env,"bottle_of_perfume_85")
    backpack_82 = registry(env,"backpack_82")
    
    # Subtask 2: Grasp the bottle of perfume
    EasyGrasp(robot, bottle_of_perfume_85)
    donothing(env)
