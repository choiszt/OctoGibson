import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Find the bell pepper.
    # Since the bell pepper is usually stored in the fridge, we move the robot to the fridge.
    fridge = registry(env, "fridge_1234")
    MoveBot(env, robot, fridge, camera)
    donothing(env)
