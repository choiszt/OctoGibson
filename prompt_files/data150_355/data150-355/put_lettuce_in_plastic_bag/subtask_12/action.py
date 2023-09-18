import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the plastic bag
    checkout_counter = registry(env, "checkout_counter_sckdal_0")
    plastic_bag = registry(env, "plastic_bag_145")
    MoveBot(env, robot, checkout_counter, camera)
    donothing(env)
