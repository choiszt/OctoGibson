import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the glove
    kid_glove_122 = registry(env,"kid_glove_122")
    MoveBot(env, robot, kid_glove_122, camera)
    donothing(env)
