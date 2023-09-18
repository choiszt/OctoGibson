import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the carton_of_milk_277
    carton_of_milk_277 = registry(env,"carton_of_milk_277")
    MoveBot(env, robot, carton_of_milk_277, camera)
    donothing(env)
