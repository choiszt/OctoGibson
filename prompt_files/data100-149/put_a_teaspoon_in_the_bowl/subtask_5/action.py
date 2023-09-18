import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find a large object that is near the teaspoon
    large_object = registry(env, "large_object")
    MoveBot(env, robot, large_object, camera)
    donothing(env)
