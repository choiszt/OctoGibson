import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the board
    board = registry(env,"board_275")
    EasyGrasp(robot, board)
    donothing(env)
