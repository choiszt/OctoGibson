import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the flashlight inside the carton
    flashlight = registry(env, "flashlight_192")
    carton = registry(env, "carton_188")
    put_inside(robot, flashlight, carton)
    donothing(env)
