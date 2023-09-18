import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the crescent roll (croissant_282)
    croissant_282 = registry(env,"croissant_282")
    MoveBot(env, robot, croissant_282, camera)
    donothing(env)
