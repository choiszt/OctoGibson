import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Continue moving the robot to find the vehicle.
    # Since the vehicle is still not in the observed objects, we need to continue exploring the environment to find it.
    # We can use the MoveBot function to move the robot around the environment.
    # However, since we don't know the exact location of the vehicle, we can't specify a target object.
    # Therefore, we will move the robot to the next nearest observed object, which is the copper_wire_282.
    copper_wire_282 = registry(env, "copper_wire_282")
    MoveBot(env, robot, copper_wire_282, camera)
    donothing(env)
