import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the board game from the bottom cabinet
    board_game = registry(env, "board_game_103")
    EasyGrasp(robot, board_game)
    donothing(env)
