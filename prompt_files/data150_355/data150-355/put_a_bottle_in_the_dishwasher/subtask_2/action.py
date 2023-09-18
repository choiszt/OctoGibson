import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the dishwasher
    dishwasher = registry(env, "dishwasher_dngvvi_0")
    MoveBot(env, robot, dishwasher, camera)
    donothing(env)
