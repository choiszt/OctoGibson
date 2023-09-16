import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the straw into the glass
    water_glass = registry(env, "water_glass_85")
    straw = registry(env, "straw_92")
    put_ontop(robot, straw, water_glass)
    donothing(env)
