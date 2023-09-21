import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Use the EasyGrasp function with the robot and the broken glass as arguments to open the robot's gripper and let the broken glass fall onto the floor.
    broken_glass_170 = registry(env,"broken_glass_170")
    EasyGrasp(robot, broken_glass_170)
    donothing(env)
