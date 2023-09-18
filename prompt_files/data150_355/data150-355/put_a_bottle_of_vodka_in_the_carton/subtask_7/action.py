import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the bottle of vodka and the carton
    bottle_of_vodka_189 = registry(env,"bottle_of_vodka_189")
    carton_188 = registry(env,"carton_188")
    
    # Subtask 2: Move the robot to the bottle of vodka
    MoveBot(env, robot, bottle_of_vodka_189, camera)
    donothing(env)
