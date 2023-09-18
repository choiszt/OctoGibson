import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the carton
    carton_87 = registry(env,"carton_87")
    MoveBot(env, robot, carton_87, camera)
