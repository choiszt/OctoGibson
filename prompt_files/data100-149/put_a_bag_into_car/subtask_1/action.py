import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the suitcase
    suitcase_286 = registry(env,"suitcase_286")
    MoveBot(env, robot, suitcase_286, camera)
    donothing(env)
