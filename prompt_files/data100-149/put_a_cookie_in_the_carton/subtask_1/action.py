import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cookie
    cookie = registry(env, "cookie_stick_196")
    MoveBot(env, robot, cookie, camera)
