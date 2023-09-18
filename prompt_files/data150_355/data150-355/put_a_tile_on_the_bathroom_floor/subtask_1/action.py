import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the tile
    tile_183 = registry(env,"tile_183")
    MoveBot(env, robot, tile_183, camera)
    donothing(env)
