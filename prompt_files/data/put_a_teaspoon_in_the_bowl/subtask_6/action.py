import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Look inside the bottom cabinet to find the teaspoon and the bowl
    bottom_cabinet = registry(env, "bottom_cabinet_no_top_qudfwe_0")
    donothing(env)
