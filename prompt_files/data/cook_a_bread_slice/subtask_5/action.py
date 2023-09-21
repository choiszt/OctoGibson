import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the toaster
    toaster = registry(env, "toaster_85")
    MoveBot(env, robot, toaster, camera)
    donothing(env)
