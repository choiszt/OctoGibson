import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the top cabinet
    top_cabinet_dmwxyl_1 = registry(env, "top_cabinet_dmwxyl_1")
    open(robot, top_cabinet_dmwxyl_1)
    donothing(env)
