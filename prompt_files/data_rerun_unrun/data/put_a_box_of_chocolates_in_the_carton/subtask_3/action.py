import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the box of chocolates
    box_of_chocolates_197 = registry(env,"box_of_chocolates_197")
    MoveBot(env, robot, box_of_chocolates_197, camera)
    donothing(env)
