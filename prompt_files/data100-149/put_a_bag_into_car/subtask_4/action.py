import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the suitcase into the car
    suitcase_286 = registry(env,"suitcase_286")
    car_275 = registry(env,"car_275")
    put_inside(robot, suitcase_286, car_275)
    donothing(env)
