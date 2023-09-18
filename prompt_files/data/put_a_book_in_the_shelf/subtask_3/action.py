import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the shelf (shelf_njwsoa_0)
    shelf_njwsoa_0 = registry(env,"shelf_njwsoa_0")
    MoveBot(env, robot, shelf_njwsoa_0, camera)
    donothing(env)
