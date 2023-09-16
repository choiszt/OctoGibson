import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the laptop
    laptop_278 = registry(env,"laptop_278")
    MoveBot(env, robot, laptop_278, camera)
    donothing(env)
