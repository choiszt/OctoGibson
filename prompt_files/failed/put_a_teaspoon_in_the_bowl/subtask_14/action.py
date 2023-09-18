import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the teaspoon inside the bottom_cabinet_no_top_qudfwe_0
    teaspoon = registry(env, "teaspoon")
