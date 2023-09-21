import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the tupperware inside the bottom cabinet
    # We need to register the tupperware first before we can interact with it.
    tupperware = registry(env, "tupperware")
    grasp(robot, tupperware)
    donothing(env)
