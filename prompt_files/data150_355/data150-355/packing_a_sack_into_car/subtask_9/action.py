import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the car and the sack
    car_275 = registry(env, "car_275")
    bap_280 = registry(env, "bap_280")
    # Subtask 2: Move the robot to the car
    MoveBot(env, robot, car_275, camera)
    donothing(env)
