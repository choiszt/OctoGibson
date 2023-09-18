import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle.
    # Since the vehicle is not observed in the environment, we need to explore the environment to find it.
    # Instead of moving the robot to specific locations, we will move the robot around the environment in a random manner until the vehicle is observed.
    # We can do this by moving the robot to a random object in the environment.
    # Here we assume that the environment has a function named "get_random_object" that returns a random object in the environment.
    random_object = env.get_random_object()
    random_object = registry(env, random_object)
    MoveBot(env, robot, random_object, camera)
    donothing(env)
