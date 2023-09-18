import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the cabinet
    cabinet = registry(env, "top_cabinet_dmwxyl_2")
    open(robot, cabinet)
    donothing(env)
