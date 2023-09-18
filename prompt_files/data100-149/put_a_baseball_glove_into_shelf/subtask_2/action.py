import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the baseball glove.
    baseball_glove = registry(env, "baseball_glove")
    MoveBot(env, robot, baseball_glove, camera)
    donothing(env)
