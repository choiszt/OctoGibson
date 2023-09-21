import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Search for the pan.
    # Since the pan is not observed in the environment, we need to search for it.
    # Here we assume the pan might be inside the trash_can_85, so we will open it.
    trash_can_85 = registry(env,"trash_can_85")
    open(robot, trash_can_85)
    donothing(env)
