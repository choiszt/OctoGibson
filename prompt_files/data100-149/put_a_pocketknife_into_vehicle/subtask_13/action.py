import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Continue to explore the environment to find the vehicle.
    # Since the vehicle is not observed in the environment, we need to continue exploring the environment to find it.
    # Instead of moving the robot to specific locations, we will move the robot around the environment in a random manner until the vehicle is observed.
    # As the 'get_random_object' function does not exist, we will move the robot to the objects that are observed in the environment one by one.
    # Here we use the observed objects provided in the conversation.
    observed_objects = ["copper_wire_282", "wicker_basket_276", "wicker_basket_277", "pocketknife_278", "charger_283"]
    for obj in observed_objects:
        obj = registry(env, obj)
        MoveBot(env, robot, obj, camera)
        donothing(env)
