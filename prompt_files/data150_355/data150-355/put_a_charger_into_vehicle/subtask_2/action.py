import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Find the vehicle
    # The vehicle is not observed in the environment, so we need to explore the environment to find it.
    # Here we assume that the vehicle is a large object placed directly on the ground, so we can move the robot to it.
    # We also assume that the vehicle is within the camera's field of view, so we set the camera to camera.
    MoveBot(env, robot, "vehicle", camera)
    donothing(env)
