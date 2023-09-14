import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the recycling bin
    recycling_bin_278 = registry(env,"recycling_bin_278")
    MoveBot(env, robot, recycling_bin_278, camera)
    donothing(env)
