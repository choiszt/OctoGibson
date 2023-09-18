import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the vehicle.
    # Since the vehicle is not observed in the environment, we need to explore the environment to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can move the robot to it.
    # We also assume that the vehicle is named "vehicle_1" in the environment.
    vehicle_1 = registry(env,"vehicle_1")
    MoveBot(env, robot, vehicle_1, camera)
    donothing(env)
