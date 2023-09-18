import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the flashlight
    flashlight = registry(env, "flashlight_192")
    MoveBot(env, robot, flashlight, camera)
    donothing(env)
