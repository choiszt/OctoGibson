import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move the robot to the pottable marigold
    pottable_marigold_275 = registry(env, "pottable_marigold_275")
    MoveBot(env, robot, pottable_marigold_275, camera)
    donothing(env)
