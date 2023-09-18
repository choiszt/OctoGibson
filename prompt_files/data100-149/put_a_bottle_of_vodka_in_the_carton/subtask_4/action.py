import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the carton
    carton_188 = registry(env,"carton_188")
    open(robot, carton_188)
    donothing(env)
