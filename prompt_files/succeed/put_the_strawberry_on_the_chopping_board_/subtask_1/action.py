import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bowl
    bowl_195 = registry(env,"bowl_195")
    MoveBot(env, robot, bowl_195, camera)
    donothing(env)
