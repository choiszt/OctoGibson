import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move the robot to a position where the broken glass will naturally fall to the floor when the robot opens its gripper.
    recycling_bin_173 = registry(env, "recycling_bin_173")
    MoveBot(env, robot, recycling_bin_173, camera)
    donothing(env)
