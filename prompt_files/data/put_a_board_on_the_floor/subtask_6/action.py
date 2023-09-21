import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 2: Put the leaf on the floor
    leaf_276 = registry(env, "leaf_276")
    floor = registry(env, "floor")
    put_ontop(robot, leaf_276, floor)
    donothing(env)
