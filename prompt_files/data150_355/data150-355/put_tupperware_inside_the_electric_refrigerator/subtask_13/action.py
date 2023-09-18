import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the tupperware
    tupperware = registry(env, "tupperware_193")
    MoveBot(env, robot, tupperware, camera)
    donothing(env)
