import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the bottom_cabinet_no_top_qudfwe_0
    bottom_cabinet_no_top_qudfwe_0 = registry(env, "bottom_cabinet_no_top_qudfwe_0")
