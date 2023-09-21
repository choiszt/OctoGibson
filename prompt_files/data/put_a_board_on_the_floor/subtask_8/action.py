import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 2: Drop the leaf on the floor
    leaf_276 = registry(env, "leaf_276")
    drop(robot, leaf_276)
    donothing(env)
