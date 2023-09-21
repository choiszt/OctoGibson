import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Put the bacon on the griddle.
    bacon = registry(env, "bacon_150")
    griddle = registry(env, "griddle_157")
    put_ontop(robot, bacon, griddle)
    donothing(env)
