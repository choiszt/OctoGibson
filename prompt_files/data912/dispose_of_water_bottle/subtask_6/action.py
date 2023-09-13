import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Close the recycling bin.
    recycling_bin_278 = registry(env,"recycling_bin_278")
    close(robot, recycling_bin_278)
    donothing(env)
