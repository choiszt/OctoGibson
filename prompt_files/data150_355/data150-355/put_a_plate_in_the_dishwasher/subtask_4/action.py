import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Open the dishwasher
    dishwasher_dngvvi_0 = registry(env,"dishwasher_dngvvi_0")
    open(robot, dishwasher_dngvvi_0)
    donothing(env)
