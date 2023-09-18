import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the sack into the car
    car_275 = registry(env,"car_275")
    bap_280 = registry(env,"bap_280")
    put_inside(robot, bap_280, car_275)
    donothing(env)
