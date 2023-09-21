import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Cook the fruitcake
    fruitcake_188 = registry(env,"fruitcake_188")
    cook(robot, fruitcake_188)
    donothing(env)
