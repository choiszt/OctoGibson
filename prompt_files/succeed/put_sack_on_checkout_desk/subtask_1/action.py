import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the checkout counter where the paper bag (sack) is located.
    checkout_counter_hhvxxr_0 = registry(env,"checkout_counter_hhvxxr_0")
    MoveBot(env, robot, checkout_counter_hhvxxr_0, camera)
    donothing(env)
