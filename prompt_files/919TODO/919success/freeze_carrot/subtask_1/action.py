import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the carrot_177
    carrot_177 = registry(env,"carrot_177")
    MoveBot(env, robot, carrot_177, camera)
    donothing(env)
