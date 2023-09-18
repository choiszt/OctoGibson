import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the bowl on the countertop
    bowl = registry(env, "bowl_85")
    MoveBot(env, robot, bowl, camera)
    donothing(env)
