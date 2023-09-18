import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the board on the floor
    board = registry(env,"board_275")
    put_ontop(robot, board, "floor")
    donothing(env)
