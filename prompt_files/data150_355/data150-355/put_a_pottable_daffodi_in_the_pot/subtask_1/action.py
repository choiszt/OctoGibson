import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the pottable daffodil
    pottable_daffodil_276 = registry(env,"pottable_daffodil_276")
    MoveBot(env, robot, pottable_daffodil_276, camera)
    donothing(env)
