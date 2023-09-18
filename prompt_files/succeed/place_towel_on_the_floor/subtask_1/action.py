import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the towel
    hand_towel_84 = registry(env,"hand_towel_84")
    MoveBot(env, robot, hand_towel_84, camera)
    donothing(env)
