import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the dishwasher
    dishwasher_dngvvi_0 = registry(env,"dishwasher_dngvvi_0")
    MoveBot(env, robot, dishwasher_dngvvi_0, camera)
    donothing(env)
