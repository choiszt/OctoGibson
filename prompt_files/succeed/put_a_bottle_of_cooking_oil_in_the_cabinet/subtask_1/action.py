import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottle_of_cooking_oil_88
    bottle_of_cooking_oil_88 = registry(env,"bottle_of_cooking_oil_88")
    MoveBot(env, robot, bottle_of_cooking_oil_88, camera)
    donothing(env)
