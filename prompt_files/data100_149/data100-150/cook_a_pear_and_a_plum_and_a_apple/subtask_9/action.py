import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Find and move to the plum.
    # Since the plum is not observed, we assume it's in the fridge.
    fridge = registry(env,"fridge")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
