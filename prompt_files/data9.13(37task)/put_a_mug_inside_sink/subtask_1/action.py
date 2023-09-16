import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the mug
    mug_201 = registry(env,"mug_201")
    MoveBot(env, robot, mug_201, camera)
    donothing(env)
