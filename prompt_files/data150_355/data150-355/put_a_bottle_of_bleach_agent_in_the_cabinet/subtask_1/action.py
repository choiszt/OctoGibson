import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cabinet
    cabinet = registry(env, "top_cabinet_dmwxyl_3")
    MoveBot(env, robot, cabinet, camera)
    donothing(env)
