import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Open the fridge to find the plum.
    fridge = registry(env,"fridge_1234")
    open(robot, fridge)
    donothing(env)
