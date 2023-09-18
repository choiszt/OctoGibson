import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the tomato and the refrigerator
    tomato = registry(env, "beefsteak_tomato_90")
    fridge = registry(env, "fridge_xyejdx_0")
    # Subtask 2: Move the robot to the tomato
    MoveBot(env, robot, tomato, camera)
    donothing(env)
