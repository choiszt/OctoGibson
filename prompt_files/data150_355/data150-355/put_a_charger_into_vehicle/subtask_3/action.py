import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Register the vehicle
    # The vehicle needs to be registered before it can be used in the MoveBot function.
    vehicle = registry(env, "vehicle")
    donothing(env)
