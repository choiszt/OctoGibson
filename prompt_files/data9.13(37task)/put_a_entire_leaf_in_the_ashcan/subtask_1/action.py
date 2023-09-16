import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the board where the leaf is located.
    board_275 = registry(env,"board_275")
    MoveBot(env, robot, board_275, camera)
