import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the chopping board.
    chopping_board_85 = registry(env,"chopping_board_85")
    EasyGrasp(robot, chopping_board_85)
    donothing(env)
