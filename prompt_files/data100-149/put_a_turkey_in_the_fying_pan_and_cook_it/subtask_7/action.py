import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the turkey
    turkey_85 = registry(env,"turkey_85")
    MoveBot(env, robot, turkey_85, camera)
    donothing(env)
