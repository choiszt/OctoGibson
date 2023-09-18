import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Move the robot to the countertop
    countertop_tpuwys_1 = registry(env,"countertop_tpuwys_1")
    MoveBot(env, robot, countertop_tpuwys_1, camera)
    donothing(env)
