import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the book inside the carton
    hardback_188 = registry(env,"hardback_188")
    carton_195 = registry(env,"carton_195")
    put_inside(robot, hardback_188, carton_195)
    donothing(env)
