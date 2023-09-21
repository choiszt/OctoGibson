import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Release the board
    board_275 = registry(env,"board_275")
    robot.release(board_275)
    donothing(env)
