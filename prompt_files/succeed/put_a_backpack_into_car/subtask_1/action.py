import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the backpack
    backpack_277 = registry(env,"backpack_277")
    MoveBot(env, robot, backpack_277, camera)
    donothing(env)
