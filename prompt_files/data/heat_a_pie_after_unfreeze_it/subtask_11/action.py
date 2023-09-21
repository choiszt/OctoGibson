import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Heat the pie
    pie = registry(env, "cheese_tart_188")
    heat(robot, pie)
    donothing(env)
