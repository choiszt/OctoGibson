import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Grasp the tupperware
    # We assume the tupperware is now visible in the environment after opening the bottom cabinet.
    # We need to register the tupperware first before we can interact with it.
    tupperware = registry(env, "tupperware")
    EasyGrasp(robot, tupperware)
    donothing(env)
