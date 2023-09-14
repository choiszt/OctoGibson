import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the laptop into the car
    laptop_278 = registry(env,"laptop_278")
    car_276 = registry(env,"car_276")
    put_inside(robot, laptop_278, car_276)
    donothing(env)
