import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the grocery shelf where the can of dog food is located.
    grocery_shelf = registry(env, "grocery_shelf_rowulr_2")
    MoveBot(env, robot, grocery_shelf, camera)
    donothing(env)
