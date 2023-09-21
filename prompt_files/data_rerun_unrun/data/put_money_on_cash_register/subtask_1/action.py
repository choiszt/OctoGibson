import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 1: Move the robot to the checkout counter where the money is located.
    checkout_counter_sckdal_0 = registry(env, "checkout_counter_sckdal_0")
    MoveBot(env, robot, checkout_counter_sckdal_0, camera)
    donothing(env)
