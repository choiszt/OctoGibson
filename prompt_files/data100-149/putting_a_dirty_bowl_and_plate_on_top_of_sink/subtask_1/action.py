import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the countertop where the bowl is located.
    bowl_85 = registry(env,"bowl_85")
    countertop_tpuwys_3 = registry(env,"countertop_tpuwys_3")
    MoveBot(env, robot, countertop_tpuwys_3, camera)
    donothing(env)
