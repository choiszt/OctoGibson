import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the car
    car_276 = registry(env,"car_276")
    open(robot, car_276)
    donothing(env)
