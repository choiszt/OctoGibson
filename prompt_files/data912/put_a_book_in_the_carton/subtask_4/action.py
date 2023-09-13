import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the carton (carton_195)
    carton_195 = registry(env,"carton_195")
    open(robot, carton_195)
    donothing(env)
