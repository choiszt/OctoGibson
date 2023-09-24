import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottom cabinet
    bottom_cabinet = registry(env, "bottom_cabinet_nyfebf_0")
    MoveBot(env, robot, bottom_cabinet, camera)
    donothing(env)