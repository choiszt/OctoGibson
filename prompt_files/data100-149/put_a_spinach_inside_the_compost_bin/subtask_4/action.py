import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the compost bin
    compost_bin_192 = registry(env, "compost_bin_192")
    MoveBot(env, robot, compost_bin_192, camera)
    donothing(env)
