import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 11: Wait for a while to let the apple and strawberry freeze
    donothing(env)
