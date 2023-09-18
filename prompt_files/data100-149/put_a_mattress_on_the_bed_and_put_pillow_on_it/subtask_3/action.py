import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bed
    bed = registry(env, "bed_zrumze_0")
    MoveBot(env, robot, bed, camera)
    donothing(env)
