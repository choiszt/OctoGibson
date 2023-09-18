import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Grasp the board
    board_275 = registry(env,"board_275")
    EasyGrasp(robot, board_275)
    donothing(env)
