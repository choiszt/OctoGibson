import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the videotape on the grocery shelf
    dvd = registry(env, "dvd_143")
    grocery_shelf = registry(env, "grocery_shelf_xngcbz_0")
    put_ontop(robot, dvd, grocery_shelf)
    donothing(env)
