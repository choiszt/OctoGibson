import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Put the box of chocolates inside the carton
    box_of_chocolates_197 = registry(env,"box_of_chocolates_197")
    carton_188 = registry(env,"carton_188")
    put_inside(robot, box_of_chocolates_197, carton_188)
    donothing(env)
