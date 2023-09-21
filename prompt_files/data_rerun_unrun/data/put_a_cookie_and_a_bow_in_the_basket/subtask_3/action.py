import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cookie
    spice_cookie_96 = registry(env,"spice_cookie_96")
    MoveBot(env, robot, spice_cookie_96, camera)
    donothing(env)
