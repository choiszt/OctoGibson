import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Register the suitcase
    suitcase_286 = registry(env, "suitcase_286")
