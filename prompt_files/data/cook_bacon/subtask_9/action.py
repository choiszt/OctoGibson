import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Heat the griddle to cook the bacon.
    griddle = registry(env, "griddle_157")
    heat(robot, griddle)
    donothing(env)
