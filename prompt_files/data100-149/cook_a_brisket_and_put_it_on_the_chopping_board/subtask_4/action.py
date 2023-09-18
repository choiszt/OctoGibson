import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the cooked brisket on the chopping board
    cutting_board = registry(env,"cutting_board_188")
    brisket = registry(env,"brisket_189")
    put_ontop(robot, brisket, cutting_board)
    donothing(env)
