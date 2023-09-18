import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the shelf
    shelf_njwsoa_1 = registry(env,"shelf_njwsoa_1")
    MoveBot(env, robot, shelf_njwsoa_1, camera)
    donothing(env)
