import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 10: Move to the front of the countertop.
    countertop_tpuwys_5 = registry(env,"countertop_tpuwys_5")
    MoveBot(env, robot, countertop_tpuwys_5, camera)
    donothing(env)
