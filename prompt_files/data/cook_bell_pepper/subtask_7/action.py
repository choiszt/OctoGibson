import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to a place where it can observe more objects.
    # Here we assume the robot can observe more objects near the shelf.
    shelf = registry(env, "shelf_owvfik_0")
    MoveBot(env, robot, shelf, camera)
    donothing(env)
