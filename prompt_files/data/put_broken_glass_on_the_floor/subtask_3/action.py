import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Drop the broken glass onto the floor
    drop(robot, "broken_glass_170")
    donothing(env)
