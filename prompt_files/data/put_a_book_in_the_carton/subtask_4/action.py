import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the book in the carton
    book = registry(env, "hardback_188")
    carton = registry(env, "carton_195")
    put_inside(robot, book, carton)
    donothing(env)
