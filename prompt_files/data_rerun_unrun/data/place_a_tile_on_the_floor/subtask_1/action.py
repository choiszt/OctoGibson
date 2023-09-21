import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the ceramic tile
    ceramic_tile_275 = registry(env,"ceramic_tile_275")
    MoveBot(env, robot, ceramic_tile_275, camera)
    donothing(env)
