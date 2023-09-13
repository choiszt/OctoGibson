import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the carton
    carton_195 = registry(env,"carton_195")
    MoveBot(env, robot, carton_195, camera)
    donothing(env)
