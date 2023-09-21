import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move to the money
    money_149 = registry(env,"money_149")
    MoveBot(env, robot, money_149, camera)
    donothing(env)
