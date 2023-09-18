import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the colored pencil inside the car
    car_275 = registry(env,"car_275")
    colored_pencil_277 = registry(env,"colored_pencil_277")
    put_inside(robot, colored_pencil_277, car_275)
    donothing(env)
