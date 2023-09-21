import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the tupperware
    tupperware_193 = registry(env,"tupperware_193")
    MoveBot(env, robot, tupperware_193, camera)
    donothing(env)
