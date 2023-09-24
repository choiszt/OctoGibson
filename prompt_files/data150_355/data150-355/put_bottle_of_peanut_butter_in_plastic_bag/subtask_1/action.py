import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the grocery shelf where the bottle of peanut butter is located.
    grocery_shelf_sjmdri_0 = registry(env,"grocery_shelf_sjmdri_0")
    MoveBot(env, robot, grocery_shelf_sjmdri_0, camera)
    donothing(env)