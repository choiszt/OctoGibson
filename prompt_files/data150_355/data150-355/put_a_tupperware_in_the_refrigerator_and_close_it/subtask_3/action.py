import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the tupperware
    tupperware_88 = registry(env,"tupperware_88")
    MoveBot(env, robot, tupperware_88, camera)
    donothing(env)
