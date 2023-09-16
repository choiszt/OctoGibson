import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the oven
    oven = registry(env,"oven_wuinhm_0")
    MoveBot(env, robot, oven, camera)
    donothing(env)
