import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the folder
    folder_190 = registry(env,"folder_190")
    MoveBot(env, robot, folder_190, camera)
    donothing(env)
