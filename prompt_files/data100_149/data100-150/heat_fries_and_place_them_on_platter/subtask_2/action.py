import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take the fries out of the fridge
    fries = registry(env, "french_fries_88")
    EasyGrasp(robot, fries)
    donothing(env)
