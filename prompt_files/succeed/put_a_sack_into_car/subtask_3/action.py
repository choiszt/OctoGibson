import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the car (car_276)
    car_276 = registry(env,"car_276")
    MoveBot(env, robot, car_276, camera)
    donothing(env)
