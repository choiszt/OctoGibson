import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the water bottle into the suitcase
    water_bottle = registry(env, "water_bottle_284")
    suitcase = registry(env, "suitcase_285")
    put_inside(robot, water_bottle, suitcase)
    donothing(env)
