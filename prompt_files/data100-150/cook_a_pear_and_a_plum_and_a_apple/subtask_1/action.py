import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop_tpuwys_2 where the apple and pear are located.
    countertop_tpuwys_2 = registry(env,"countertop_tpuwys_2")
    MoveBot(env, robot, countertop_tpuwys_2, camera)
    donothing(env)
