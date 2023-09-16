import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the ice cube into the glass
    water_glass = registry(env, "water_glass_85")
    ice_cube = registry(env, "ice_cube_87")
    put_ontop(robot, ice_cube, water_glass)
    donothing(env)
