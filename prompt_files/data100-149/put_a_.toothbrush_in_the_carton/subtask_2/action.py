import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the toothbrush
    toothbrush_193 = registry(env,"toothbrush_193")
    EasyGrasp(robot, toothbrush_193)
    donothing(env)
