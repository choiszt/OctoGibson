import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find the vehicle in the environment.
    # Since the vehicle is not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can use the MoveBot function to move the robot.
    # We also assume that the vehicle's name is "vehicle_1". This is a placeholder name and should be replaced with the actual name of the vehicle when it is found.
    vehicle_1 = registry(env, "vehicle_1")
    MoveBot(env, robot, vehicle_1, camera)
    donothing(env)
