import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Take the platter out of the top cabinet
    platter = registry(env,"platter_86")
    EasyGrasp(robot, platter)
    donothing(env)
