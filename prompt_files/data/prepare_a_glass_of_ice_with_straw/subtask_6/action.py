import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the straw into the glass
    straw = registry(env, "straw_92")
    glass = registry(env, "water_glass_85")
    put_ontop(robot, straw, glass)
    donothing(env)
