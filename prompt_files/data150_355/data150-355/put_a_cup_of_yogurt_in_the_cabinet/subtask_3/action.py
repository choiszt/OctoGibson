import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the cup of yogurt
    cup_of_yogurt_88 = registry(env,"cup_of_yogurt_88")
    MoveBot(env, robot, cup_of_yogurt_88, camera)
    donothing(env)
