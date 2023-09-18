import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the cabinet
    top_cabinet_dmwxyl_3 = registry(env,"top_cabinet_dmwxyl_3")
    open(robot, top_cabinet_dmwxyl_3)
    donothing(env)
