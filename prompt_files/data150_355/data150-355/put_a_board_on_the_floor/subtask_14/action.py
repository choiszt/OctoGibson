import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the board on the floor
    board_275 = registry(env, "board_275")
    put_ontop(robot, board_275, "floor")
    donothing(env)
