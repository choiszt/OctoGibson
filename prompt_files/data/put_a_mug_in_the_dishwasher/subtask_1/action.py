import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the mug
    mug_88 = registry(env,"mug_88")
    MoveBot(env, robot, mug_88, camera)
    donothing(env)
