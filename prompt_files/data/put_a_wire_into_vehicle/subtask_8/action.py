import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Explore the environment to find the vehicle.
    # Since the vehicle was not found in the previous step, we need to explore the environment to find it.
    # Here we assume that the vehicle is named "vehicle_1" in the environment.
    vehicle_1 = registry(env,"vehicle_1")
