import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the grocery shelf.
    grocery_shelf_prtqlw_0 = registry(env,"grocery_shelf_prtqlw_0")
    MoveBot(env, robot, grocery_shelf_prtqlw_0, camera)
    donothing(env)
