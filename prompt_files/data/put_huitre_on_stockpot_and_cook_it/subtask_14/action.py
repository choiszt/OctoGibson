import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Find and move to the fridge
    fridge = registry(env, "fridge_dszchb_0")
    MoveBot(env, robot, fridge, camera)
    donothing(env)