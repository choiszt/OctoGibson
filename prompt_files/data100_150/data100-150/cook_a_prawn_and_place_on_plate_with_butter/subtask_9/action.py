import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Register the prawn and the plate
    shrimp = registry(env,"shrimp_201")
    plate = registry(env,"plate_215")
