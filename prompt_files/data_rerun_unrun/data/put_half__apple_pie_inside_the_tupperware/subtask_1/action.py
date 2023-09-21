import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the half apple pie
    half_apple_pie_189 = registry(env,"half_apple_pie_189")
    MoveBot(env, robot, half_apple_pie_189, camera)
    donothing(env)
