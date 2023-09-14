import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Open the top cabinet
    top_cabinet = registry(env, "top_cabinet_dmwxyl_1")
    open(robot, top_cabinet)
    donothing(env)
