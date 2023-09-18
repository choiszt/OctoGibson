import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cheese_tart_280
    cheese_tart_280 = registry(env,"cheese_tart_280")
    MoveBot(env, robot, cheese_tart_280, camera)
    donothing(env)
