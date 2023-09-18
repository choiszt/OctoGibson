import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the canned food
    canned_food_91 = registry(env,"canned_food_91")
    MoveBot(env, robot, canned_food_91, camera)
    donothing(env)
