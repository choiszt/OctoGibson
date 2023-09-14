import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the bin
    bin = registry(env, "recycling_bin_188")
    MoveBot(env, robot, bin, camera)
    donothing(env)
