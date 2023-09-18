import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Freeze the carrot
    carrot = registry(env, "carrot_178")
    freeze(robot, carrot)
    donothing(env)
