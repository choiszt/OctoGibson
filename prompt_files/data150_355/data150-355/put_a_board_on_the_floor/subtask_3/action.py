import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the trash can
    trash_can_284 = registry(env,"trash_can_284")
    MoveBot(env, robot, trash_can_284, camera)
    donothing(env)
