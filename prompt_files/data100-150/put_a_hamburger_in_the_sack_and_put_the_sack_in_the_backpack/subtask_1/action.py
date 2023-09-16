import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop where the hamburger is located.
    countertop_tpuwys_0 = registry(env,"countertop_tpuwys_0")
    MoveBot(env, robot, countertop_tpuwys_0, camera)
    donothing(env)
