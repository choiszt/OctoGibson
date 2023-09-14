import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the plate with the cheese tart inside the fridge
    plate = registry(env,"plate_87")
    fridge = registry(env,"fridge_xyejdx_0")
    put_inside(robot, plate, fridge)
    donothing(env)
