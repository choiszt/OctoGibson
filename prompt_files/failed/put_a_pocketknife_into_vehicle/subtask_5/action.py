import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle.
    # Since the vehicle is not observed in the environment, we need to explore the environment to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can move the robot to it.
    # We also assume that the vehicle is named "vehicle_1" in the environment.
    # However, before we move the robot to the vehicle, we need to make sure that the vehicle is observed in the environment.
    # Therefore, we need to explore the environment first.
    # We can do this by moving the robot to different locations in the environment until the vehicle is observed.
    # Here we assume that the environment has a location named "location_1" where the vehicle can be observed.
    # But before that, we need to register the location_1 in the environment.
    location_1 = registry(env,"location_1")
    MoveBot(env, robot, location_1, camera)
    donothing(env)
