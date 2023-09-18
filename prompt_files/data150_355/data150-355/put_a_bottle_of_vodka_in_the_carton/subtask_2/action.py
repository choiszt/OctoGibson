import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the bottle of vodka
    bottle_of_vodka_189 = registry(env,"bottle_of_vodka_189")
    EasyGrasp(robot, bottle_of_vodka_189)
    donothing(env)
