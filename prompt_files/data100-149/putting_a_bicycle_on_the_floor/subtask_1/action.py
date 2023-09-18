import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bicycle
    bicycle_592 = registry(env,"bicycle_592")
    MoveBot(env, robot, bicycle_592, camera)
    donothing(env)
