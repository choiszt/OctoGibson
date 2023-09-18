import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the jigsaw puzzle
    jigsaw_puzzle_85 = registry(env,"jigsaw_puzzle_85")
    MoveBot(env, robot, jigsaw_puzzle_85, camera)
    donothing(env)
