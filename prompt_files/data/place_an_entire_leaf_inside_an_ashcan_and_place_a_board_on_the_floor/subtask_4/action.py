import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move back to the board
    board_275 = registry(env,"board_275")
    MoveBot(env, robot, board_275, camera)
    donothing(env)