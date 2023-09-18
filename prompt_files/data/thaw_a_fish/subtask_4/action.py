import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Thaw the fish
    salmon = registry(env, "salmon_172")
    heat(robot, salmon)
    donothing(env)
