import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot closer to the vehicle
    # Now that the vehicle has been registered, we can move the robot closer to it.
    vehicle_1 = registry(env,"vehicle_1")
    MoveBot(env, robot, vehicle_1, camera)
    donothing(env)
