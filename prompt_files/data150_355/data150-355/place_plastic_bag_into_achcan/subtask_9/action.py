import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the trash can
    trash_can_279 = registry(env,"trash_can_279")
    MoveBot(env, robot, trash_can_279, camera)
    donothing(env)
