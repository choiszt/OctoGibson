import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Search for the pan.
    # Since the pan is not observed in the environment, we need to search for it.
    # Here we assume the pan might be somewhere else in the environment, so we will move the robot to search for it.
    MoveBot(env, robot, "pan", camera)
    donothing(env)
