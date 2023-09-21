import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the tupperware
    tupperware_91 = registry(env,"tupperware_91")
    MoveBot(env, robot, tupperware_91, camera)
    donothing(env)
