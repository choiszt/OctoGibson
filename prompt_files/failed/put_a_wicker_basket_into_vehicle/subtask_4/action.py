import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle
    # Since the vehicle is not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can move the robot to it.
    # We also assume that the vehicle's name is "vehicle_1". This is a placeholder name and should be replaced with the actual name when the vehicle is found.
    # However, before moving to the vehicle, we need to make sure that the vehicle is actually observed in the environment.
    # Therefore, we add a condition to check if the vehicle is observed before moving the robot to it.
    vehicle_1 = registry(env,"vehicle_1")
    if vehicle_1 in env.get_observed_objects():
        MoveBot(env, robot, vehicle_1, camera)
        donothing(env)
    else:
        print("Vehicle not found. Continue exploring the environment.")
