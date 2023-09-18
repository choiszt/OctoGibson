import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the paving stone
    paving_stone_275 = registry(env,"paving_stone_275")
    MoveBot(env, robot, paving_stone_275, camera)
    donothing(env)
