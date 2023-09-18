import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the broken glass onto the floor
    broken_glass_170 = registry(env, "broken_glass_170")
    put_ontop(robot, broken_glass_170, None)
    donothing(env)
