import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bowl
    bowl_788 = registry(env,"bowl_788")
    MoveBot(env, robot, bowl_788, camera)
    donothing(env)
