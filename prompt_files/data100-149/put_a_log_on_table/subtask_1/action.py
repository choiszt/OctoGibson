import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the log
    log_275 = registry(env,"log_275")
    MoveBot(env, robot, log_275, camera)
    donothing(env)
