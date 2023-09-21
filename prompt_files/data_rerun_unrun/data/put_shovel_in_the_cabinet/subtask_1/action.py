import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the shovel and the cabinet
    shovel = registry(env, "shovel_94")
    cabinet = registry(env, "bottom_cabinet_jrhgeu_0")
    
    # Subtask 2: Grasp the shovel
    EasyGrasp(robot, shovel)
    donothing(env)
