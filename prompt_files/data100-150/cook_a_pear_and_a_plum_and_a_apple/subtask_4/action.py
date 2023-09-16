import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot closer to the pear.
    countertop_tpuwys_2 = registry(env,"countertop_tpuwys_2")
    MoveBot(env, robot, countertop_tpuwys_2, camera)
    donothing(env)
