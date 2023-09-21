import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the board game on the table.
    board_game_103 = registry(env,"board_game_103")
    breakfast_table_dnsjnv_0 = registry(env,"breakfast_table_dnsjnv_0")
    put_ontop(robot, board_game_103, breakfast_table_dnsjnv_0)
    donothing(env)
