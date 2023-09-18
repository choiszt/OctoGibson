import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the log
    log_276 = registry(env,"log_276")
    EasyGrasp(robot, log_276)
    donothing(env)
