import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the checkout desk
    checkout_counter_sckdal_0 = registry(env,"checkout_counter_sckdal_0")
    MoveBot(env, robot, checkout_counter_sckdal_0, camera)
    donothing(env)
