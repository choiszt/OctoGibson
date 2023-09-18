import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the log
    log_275 = registry(env,"log_275")
    EasyGrasp(robot, log_275)
    donothing(env)
