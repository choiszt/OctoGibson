import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the carton
    carton_96 = registry(env,"carton_96")
    MoveBot(env, robot, carton_96, camera)
    donothing(env)
