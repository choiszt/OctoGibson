import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to a location where it can find the bok choy and the frying pan.
    # Since we don't know where the bok choy and the frying pan are, we move the robot to the kitchen area, which is a reasonable place to find them.
    kitchen_area = registry(env, "kitchen_area")
    MoveBot(env, robot, kitchen_area, camera)
    donothing(env)
