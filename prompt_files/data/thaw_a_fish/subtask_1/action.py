import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env, robot, fridge, camera)
