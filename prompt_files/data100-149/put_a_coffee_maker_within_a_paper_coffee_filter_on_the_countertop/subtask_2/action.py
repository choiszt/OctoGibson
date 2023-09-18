import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the top cabinet
    top_cabinet = registry(env, "top_cabinet_dmwxyl_2")
    MoveBot(env, robot, top_cabinet, camera)
    donothing(env)
