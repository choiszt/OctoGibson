import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the toothbrush
    toothbrush_193 = registry(env,"toothbrush_193")
    MoveBot(env, robot, toothbrush_193, camera)
    donothing(env)
