import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the shelf
    shelf = registry(env, "shelf_njwsoa_0")
    MoveBot(env, robot, shelf, camera)
    donothing(env)
