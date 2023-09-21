import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the box of candy and the backpack.
    box_of_candy_89 = registry(env,"box_of_candy_89")
    backpack_82 = registry(env,"backpack_82")
    
    # Subtask 2: Check if the box of candy is already inside the backpack.
    if ('box_of_candy_89', 'inside', 'backpack_82') not in env.relations:
        # Subtask 3: If not, put the box of candy in the backpack.
        put_inside(robot, box_of_candy_89, backpack_82)
        donothing(env)
