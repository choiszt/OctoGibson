import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the backpack.
    backpack_192 = registry(env,"backpack_192")
    open(robot, backpack_192)
    donothing(env)
