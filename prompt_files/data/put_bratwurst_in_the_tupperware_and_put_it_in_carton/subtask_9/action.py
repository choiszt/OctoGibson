import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the tupperware inside the bottom cabinet
    # We need to register the tupperware first before we can interact with it.
    tupperware = registry(env, "tupperware_1234") # replace "tupperware_1234" with the actual name of the tupperware
    donothing(env)
