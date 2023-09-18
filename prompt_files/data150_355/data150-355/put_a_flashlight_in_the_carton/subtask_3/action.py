import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the carton
    carton = registry(env, "carton_188")
    MoveBot(env, robot, carton, camera)
    donothing(env)
