import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the backpack.
    backpack_192 = registry(env,"backpack_192")
    MoveBot(env, robot, backpack_192, camera)
    donothing(env)
