import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the suitcase
    suitcase_276 = registry(env,"suitcase_276")
    MoveBot(env, robot, suitcase_276, camera)
    donothing(env)
