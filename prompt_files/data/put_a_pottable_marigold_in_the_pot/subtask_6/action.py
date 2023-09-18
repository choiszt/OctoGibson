import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the objects
    pottable_marigold_275 = registry(env, "pottable_marigold_275")
    plant_pot_278 = registry(env, "plant_pot_278")
