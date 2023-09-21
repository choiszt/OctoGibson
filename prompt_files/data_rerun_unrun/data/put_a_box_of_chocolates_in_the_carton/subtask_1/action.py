import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the box of chocolates and the carton
    box_of_chocolates_197 = registry(env,"box_of_chocolates_197")
    carton_188 = registry(env,"carton_188")
    # Subtask 2: Move the robot to the carton
    MoveBot(env, robot, carton_188, camera)
    donothing(env)
