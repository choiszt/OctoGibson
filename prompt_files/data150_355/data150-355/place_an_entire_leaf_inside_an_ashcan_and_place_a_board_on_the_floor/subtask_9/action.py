import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Release the board to let it fall on the floor
    board = registry(env,"board_275")
    robot.release(board)
    donothing(env)
