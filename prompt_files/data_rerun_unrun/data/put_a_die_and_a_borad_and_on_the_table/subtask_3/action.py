import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the board game out of the bottom cabinet.
    board_game_103 = registry(env,"board_game_103")
    EasyGrasp(robot, board_game_103)
    donothing(env)
