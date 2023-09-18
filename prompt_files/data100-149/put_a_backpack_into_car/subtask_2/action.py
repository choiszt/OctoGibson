import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the backpack
    backpack_277 = registry(env,"backpack_277")
    EasyGrasp(robot, backpack_277)
    donothing(env)
