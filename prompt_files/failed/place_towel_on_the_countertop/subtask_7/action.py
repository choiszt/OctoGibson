import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Close the cabinet.
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    close(robot, top_cabinet_dmwxyl_2)
    donothing(env)
