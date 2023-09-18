import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the car
    car_275 = registry(env,"car_275")
    MoveBot(env, robot, car_275, camera)
    donothing(env)
