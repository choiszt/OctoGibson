import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the newspaper
    newspaper = registry(env, "newspaper_89")
    MoveBot(env, robot, newspaper, camera)
