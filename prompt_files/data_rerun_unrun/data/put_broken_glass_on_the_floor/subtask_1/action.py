import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the broken glass
    broken_glass_170 = registry(env,"broken_glass_170")
    EasyGrasp(robot, broken_glass_170)
    donothing(env)
