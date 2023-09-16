import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the water bottle into the recycling bin
    water_bottle_275 = registry(env,"water_bottle_275")
    recycling_bin_278 = registry(env,"recycling_bin_278")
    put_inside(robot, water_bottle_275, recycling_bin_278)
    donothing(env)
