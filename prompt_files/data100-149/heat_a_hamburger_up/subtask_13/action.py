import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 13: Check if the hamburger is heated. If not, repeat steps 8-12.
    hamburger_85 = registry(env,"hamburger_85")
    if hamburger_85['heatable'] == 0:
        return True
    else:
        return False
