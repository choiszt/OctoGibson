import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Move the robot to the carton
    carton_188 = registry(env,"carton_188")
    MoveBot(env, robot, carton_188, camera)
    donothing(env)
