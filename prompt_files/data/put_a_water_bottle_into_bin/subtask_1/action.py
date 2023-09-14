import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the water bottle
    water_bottle_275 = registry(env,"water_bottle_275")
    MoveBot(env, robot, water_bottle_275, camera)
    donothing(env)
