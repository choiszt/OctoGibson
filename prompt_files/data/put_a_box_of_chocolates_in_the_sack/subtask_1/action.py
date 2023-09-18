import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop
    countertop = registry(env, "countertop_tpuwys_2")
    MoveBot(env, robot, countertop, camera)
    donothing(env)
