import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the backpack
    backpack_82 = registry(env,"backpack_82")
    MoveBot(env, robot, backpack_82, camera)
    donothing(env)