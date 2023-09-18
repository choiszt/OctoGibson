import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Move the robot back to the board
    board = registry(env,"board_275")
    MoveBot(env, robot, board, camera)
    donothing(env)
