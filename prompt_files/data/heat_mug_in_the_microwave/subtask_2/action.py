import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the mug from the cabinet
    mug = registry(env, "mug_188")
    EasyGrasp(robot, mug)
    donothing(env)
