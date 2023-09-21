import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to a place where it can observe more objects.
    # Since the fridge is not observed in the environment, we need to move the robot to a place where it can observe more objects.
    # Here we move the robot to the shelf as it is the only large object observed in the environment.
    shelf = registry(env, "shelf_owvfik_0")
    MoveBot(env, robot, shelf, camera)
    donothing(env)
