import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the suitcase into the car
    suitcase = registry(env, "suitcase_285")
    car = registry(env, "car_275")
    put_inside(robot, suitcase, car)
    donothing(env)
