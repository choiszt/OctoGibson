import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the book
    book = registry(env, "hardback_188")
    EasyGrasp(robot, book)
    donothing(env)
