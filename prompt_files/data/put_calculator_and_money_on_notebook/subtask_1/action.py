import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the grocery_shelf_prtqlw_1
    grocery_shelf_prtqlw_1 = registry(env, "grocery_shelf_prtqlw_1")
    MoveBot(env, robot, grocery_shelf_prtqlw_1, camera)
    donothing(env)
