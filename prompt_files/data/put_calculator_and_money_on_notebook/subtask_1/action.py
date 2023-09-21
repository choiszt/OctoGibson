import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the calculator
    calculator_145 = registry(env,"calculator_145")
    MoveBot(env, robot, calculator_145, camera)
