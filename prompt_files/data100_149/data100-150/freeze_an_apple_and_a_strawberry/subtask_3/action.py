import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the bowl
    bowl = registry(env, "bowl_87")
    MoveBot(env, robot, bowl, camera)
    donothing(env)
