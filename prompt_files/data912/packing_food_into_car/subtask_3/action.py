import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the croissant into the suitcase
    suitcase = registry(env, "suitcase_285")
    croissant = registry(env, "croissant_283")
    put_inside(robot, croissant, suitcase)
    donothing(env)
