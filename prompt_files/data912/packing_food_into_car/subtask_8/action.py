import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Move the robot to the car
    car = registry(env, "car_275")
    MoveBot(env, robot, car, camera)
    donothing(env)
