import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the ice cube in the pitcher
    ice_cube = registry(env, "ice_cube_93")
    pitcher = registry(env, "jug_87")
    put_inside(robot, ice_cube, pitcher)
    donothing(env)
