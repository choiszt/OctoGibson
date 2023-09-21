import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Open the robot's gripper to let the broken glass fall onto the floor.
    robot.release()
    donothing(env)
