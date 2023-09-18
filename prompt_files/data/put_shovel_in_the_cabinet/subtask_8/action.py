import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the shovel and the cabinet
    shovel_94 = registry(env,"shovel_94")
    bottom_cabinet_jrhgeu_0 = registry(env,"bottom_cabinet_jrhgeu_0")
