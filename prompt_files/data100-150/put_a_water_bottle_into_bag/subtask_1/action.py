import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the water bottle and the suitcase
    water_bottle = registry(env, "water_bottle_284")
    suitcase = registry(env, "suitcase_285")
    # Subtask 2: Move the robot to the water bottle
    MoveBot(env, robot, water_bottle, camera)
