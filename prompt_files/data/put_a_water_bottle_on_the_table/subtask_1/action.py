import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the water bottle
    water_bottle_91 = registry(env,"water_bottle_91")
    MoveBot(env, robot, water_bottle_91, camera)
    donothing(env)
