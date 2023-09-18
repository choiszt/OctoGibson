import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the bottle of vodka inside the carton
    bottle_of_vodka_189 = registry(env,"bottle_of_vodka_189")
    carton_188 = registry(env,"carton_188")
    put_inside(robot, bottle_of_vodka_189, carton_188)
    donothing(env)
