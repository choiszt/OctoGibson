import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the teacup
    teacup_191 = registry(env,"teacup_191")
    MoveBot(env, robot, teacup_191, camera)
    donothing(env)
