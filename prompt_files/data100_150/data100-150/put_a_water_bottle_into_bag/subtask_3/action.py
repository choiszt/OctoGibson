import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the suitcase
    suitcase = registry(env, "suitcase_285")
    MoveBot(env, robot, suitcase, camera)
    donothing(env)
