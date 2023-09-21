import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the pumpkin
    pumpkin_188 = registry(env,"pumpkin_188")
    MoveBot(env, robot, pumpkin_188, camera)
