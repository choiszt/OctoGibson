import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move to the checkout counter with the prawn
    checkout_counter_hhvxxr_0 = registry(env,"checkout_counter_hhvxxr_0")
    MoveBot(env, robot, checkout_counter_hhvxxr_0, camera)
    donothing(env)
