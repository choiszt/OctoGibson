import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Register the prawn
    shrimp_201 = registry(env,"shrimp_201")
