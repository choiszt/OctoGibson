import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the stockpot
    stockpot = registry(env,"stockpot_123")
    MoveBot(env, robot, stockpot, camera)
    donothing(env)
