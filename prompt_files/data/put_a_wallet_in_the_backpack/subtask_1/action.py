import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the wallet
    wallet_87 = registry(env,"wallet_87")
    MoveBot(env, robot, wallet_87, camera)
    donothing(env)
