import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the leaf inside the ashcan
    leaf = registry(env,"leaf_276")
    ashcan = registry(env,"trash_can_284")
    put_inside(robot, leaf, ashcan)
    donothing(env)
