import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the bell pepper.
    # Here we assume the bell pepper is named "bell_pepper_123".
    bell_pepper = registry(env, "bell_pepper_123")
