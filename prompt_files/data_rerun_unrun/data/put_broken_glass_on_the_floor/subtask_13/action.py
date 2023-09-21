import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Release the broken glass from the robot's gripper.
    broken_glass_170 = registry(env,"broken_glass_170")
    robot.release(broken_glass_170)
    donothing(env)
