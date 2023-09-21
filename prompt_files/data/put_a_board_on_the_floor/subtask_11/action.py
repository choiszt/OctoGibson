import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 2: Put the leaf in the trash can
    leaf_276 = registry(env, "leaf_276")
    trash_can_284 = registry(env, "trash_can_284")
    put_inside(robot, leaf_276, trash_can_284)
    donothing(env)
