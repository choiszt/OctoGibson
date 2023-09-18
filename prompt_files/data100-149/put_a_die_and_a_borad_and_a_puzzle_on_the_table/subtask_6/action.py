import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Grasp the board from the cabinet
    board_game = registry(env, "board_game_103")
    EasyGrasp(robot, board_game)
    donothing(env)
