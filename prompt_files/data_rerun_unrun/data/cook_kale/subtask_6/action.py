import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move closer to the saucepot
    saucepot = registry(env, "saucepot_87")
    countertop = registry(env, "countertop_tpuwys_1")
    MoveBot(env, robot, countertop, camera)
    donothing(env)
