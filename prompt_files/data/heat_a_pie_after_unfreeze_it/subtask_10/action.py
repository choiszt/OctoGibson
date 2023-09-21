import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Unfreeze the pie
    pie = registry(env, "cheese_tart_188")
    unfreeze(robot, pie)
    donothing(env)
