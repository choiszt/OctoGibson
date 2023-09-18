import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the backpack into the car
    backpack_277 = registry(env,"backpack_277")
    car_276 = registry(env,"car_276")
    put_inside(robot, backpack_277, car_276)
    donothing(env)
