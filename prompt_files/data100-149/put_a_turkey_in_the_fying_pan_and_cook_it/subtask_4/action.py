import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the frying pan
    frying_pan_88 = registry(env,"frying_pan_88")
    MoveBot(env, robot, frying_pan_88, camera)
    donothing(env)
