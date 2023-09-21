import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the objects: fridge, stove, frying_pan, and bell_pepper.
    fridge = registry(env, "fridge")
    stove = registry(env, "stove")
    frying_pan = registry(env, "frying_pan_150")
    bell_pepper = registry(env, "bell_pepper")
