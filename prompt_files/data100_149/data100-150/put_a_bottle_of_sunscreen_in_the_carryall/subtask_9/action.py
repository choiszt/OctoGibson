import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottle of sunscreen
    bottle_of_sunscreen_34 = registry(env,"bottle_of_sunscreen_34")
    MoveBot(env, robot, bottle_of_sunscreen_34, camera)
    donothing(env)
