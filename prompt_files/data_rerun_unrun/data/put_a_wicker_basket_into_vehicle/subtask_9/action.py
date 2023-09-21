import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the vehicle
    # Since the vehicle is not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can move the robot to it.
    # We also assume that the vehicle's name is "vehicle_1". This is a placeholder name and should be replaced with the actual name when the vehicle is found.
    # However, before moving to the vehicle, we need to make sure that the vehicle is actually observed in the environment.
    # Therefore, we add a condition to check if the vehicle is observed before moving the robot to it.
    # Since the 'get_observed_objects' method does not exist, we will use a different approach to check if the vehicle is observed.
    # We will use a try-except block to attempt to register the vehicle. If the registration is successful, then the vehicle is observed in the environment.
    try:
        vehicle_1 = registry(env,"vehicle_1")
        MoveBot(env, robot, vehicle_1, camera)
        donothing(env)
    except:
        print("Vehicle not found. Continue exploring the environment.")
