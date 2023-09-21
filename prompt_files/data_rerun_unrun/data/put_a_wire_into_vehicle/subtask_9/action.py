import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle.
    # Since the vehicle is not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can use the MoveBot function to move the robot.
    # We also assume that the vehicle's name is "vehicle_1". This is a placeholder name and should be replaced with the actual name of the vehicle when it is found.
    # However, before we can move to the vehicle, we need to find it. Therefore, we will first move the robot to a different location in the environment to explore.
    # We will move the robot to the charger, which is the closest object to the robot according to the observed objects.
    charger_283 = registry(env, "charger_283")
    MoveBot(env, robot, charger_283, camera)
    donothing(env)
