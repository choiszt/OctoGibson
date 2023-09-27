import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the toaster oven
    toaster_oven_wuinhm_0 = registry(env,"toaster_oven_wuinhm_0")
    MoveBot(env, robot, toaster_oven_wuinhm_0, camera)
    donothing(env)

