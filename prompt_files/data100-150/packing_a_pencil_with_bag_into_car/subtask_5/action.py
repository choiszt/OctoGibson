import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the car
    car_275 = registry(env,"car_275")
    open(robot, car_275)
    donothing(env)
