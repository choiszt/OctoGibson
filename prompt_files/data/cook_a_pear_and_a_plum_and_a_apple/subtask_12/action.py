import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Put the cooked apple back into the bowl
    apple_87 = registry(env,"apple_87")
    bowl_88 = registry(env,"bowl_88")
    put_inside(robot, apple_87, bowl_88)
    donothing(env)
