import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to a place where it can observe more objects.
    shelf_owvfik_0 = registry(env, "shelf_owvfik_0")
    MoveBot(env, robot, shelf_owvfik_0, camera)
    donothing(env)
