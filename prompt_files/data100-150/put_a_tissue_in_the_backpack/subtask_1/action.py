import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Open the backpack
    backpack_82 = registry(env,"backpack_82")
    open(robot,backpack_82)
    donothing(env)
