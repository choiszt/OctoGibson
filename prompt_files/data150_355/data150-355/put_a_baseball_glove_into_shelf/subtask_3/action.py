import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the suitcase_277.
    suitcase_277 = registry(env, "suitcase_277")
    MoveBot(env, robot, suitcase_277, camera)
    donothing(env)
