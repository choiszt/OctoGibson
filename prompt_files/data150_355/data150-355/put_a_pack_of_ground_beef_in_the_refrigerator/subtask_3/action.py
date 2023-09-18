import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the pack of ground beef in the fridge
    fridge = registry(env, "fridge_xyejdx_0")
    pack_of_ground_beef = registry(env, "pack_of_ground_beef_87")
    put_inside(robot, pack_of_ground_beef, fridge)
    donothing(env)
