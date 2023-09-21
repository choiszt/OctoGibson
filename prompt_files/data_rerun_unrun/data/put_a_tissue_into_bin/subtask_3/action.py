import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the bin
    recycling_bin_281 = registry(env,"recycling_bin_281")
    MoveBot(env, robot, recycling_bin_281, camera)
    donothing(env)
