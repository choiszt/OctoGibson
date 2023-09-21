import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Find the vehicle.
    vehicle = registry(env, "vehicle")
    MoveBot(env, robot, vehicle, camera)
    donothing(env)
