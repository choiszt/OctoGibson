import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the pottable daffodil
    pottable_daffodil_276 = registry(env,"pottable_daffodil_276")
    EasyGrasp(robot, pottable_daffodil_276)
    donothing(env)
