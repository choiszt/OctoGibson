import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the steak
    steak_143 = registry(env,"steak_143")
    MoveBot(env, robot, steak_143, camera)
    donothing(env)
