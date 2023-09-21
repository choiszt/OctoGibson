import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Register the vehicle in the environment
    # Since the vehicle is not observed in the environment, we need to register it first.
    # Here we assume that the vehicle is named "vehicle_1" in the environment.
    vehicle_1 = registry(env,"vehicle_1")
