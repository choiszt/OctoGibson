import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to carton_88
    carton_88 = registry(env, "carton_88")
    MoveBot(env, robot, carton_88, camera)
    donothing(env)
