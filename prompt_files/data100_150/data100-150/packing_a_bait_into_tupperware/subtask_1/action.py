import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot closer to the bait_278
    bait_278 = registry(env,"bait_278")
    MoveBot(env, robot, bait_278, camera)
    donothing(env)
