import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle
    # Since the vehicle is not observed in the environment, we need to explore the environment to find it.
    # Here we assume that the function explore_environment can help the robot to explore the environment and find the vehicle.
    explore_environment(robot, env, camera)
    donothing(env)
