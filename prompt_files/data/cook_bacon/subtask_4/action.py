import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the stove
    stove = registry(env, "stove_rgpphy_0")
    MoveBot(env, robot, stove, camera)
    donothing(env)
