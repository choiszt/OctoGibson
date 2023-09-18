import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the grocery shelf
    grocery_shelf = registry(env, "grocery_shelf_rowulr_5")
    MoveBot(env, robot, grocery_shelf, camera)
    donothing(env)
