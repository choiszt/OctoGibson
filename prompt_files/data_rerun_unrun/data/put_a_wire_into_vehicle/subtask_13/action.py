import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Continue to explore the environment to find the vehicle.
    # Since the vehicle is still not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can use the MoveBot function to move the robot.
    # We also assume that the vehicle's name is "vehicle_1". This is a placeholder name and should be replaced with the actual name of the vehicle when it is found.
    # However, before we can move to the vehicle, we need to find it. Therefore, we will continue to move the robot to a different location in the environment to explore.
    # We will move the robot to the pocketknife_278, which is the next closest object to the robot according to the observed objects.
    pocketknife_278 = registry(env, "pocketknife_278")
    MoveBot(env, robot, pocketknife_278, camera)
    donothing(env)
