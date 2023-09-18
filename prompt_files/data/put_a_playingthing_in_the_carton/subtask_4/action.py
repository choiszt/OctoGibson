import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the carton
    carton_96 = registry(env,"carton_96")
    open(robot, carton_96)
    donothing(env)
