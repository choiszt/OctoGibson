import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the shears
    shears_89 = registry(env,"shears_89")
    MoveBot(env, robot, shears_89, camera)
    donothing(env)
