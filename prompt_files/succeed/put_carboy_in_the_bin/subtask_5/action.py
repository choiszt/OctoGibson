import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Open the recycling bin
    recycling_bin = registry(env, "recycling_bin_188")
    open(robot, recycling_bin)
    donothing(env)
