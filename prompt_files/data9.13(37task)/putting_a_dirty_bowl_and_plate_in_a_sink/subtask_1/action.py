import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the plate
    plate_88 = registry(env,"plate_88")
    MoveBot(env, robot, plate_88, camera)
    donothing(env)
