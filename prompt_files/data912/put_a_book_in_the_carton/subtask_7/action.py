import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the book and the carton
    hardback_188 = registry(env,"hardback_188")
    carton_195 = registry(env,"carton_195")
