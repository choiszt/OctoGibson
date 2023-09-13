import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the recycling bin and the water bottle.
    recycling_bin_278 = registry(env,"recycling_bin_278")
    water_bottle_275 = registry(env,"water_bottle_275")
    # Subtask 2: Move the robot to the water bottle.
    MoveBot(env, robot, water_bottle_275, camera)
    donothing(env)
