import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the granola bar
    granola_bar_86 = registry(env,"granola_bar_86")
    MoveBot(env, robot, granola_bar_86, camera)
