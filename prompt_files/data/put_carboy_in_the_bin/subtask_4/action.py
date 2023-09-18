import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the recycling bin (bin)
    recycling_bin = registry(env, "recycling_bin_188")
    MoveBot(env, robot, recycling_bin, camera)
    donothing(env)
