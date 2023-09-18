import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the plate and the dishwasher
    plate_85 = registry(env,"plate_85")
    dishwasher_dngvvi_0 = registry(env,"dishwasher_dngvvi_0")
    
    # Subtask 2: Move the robot to the plate
    MoveBot(env, robot, plate_85, camera)
    donothing(env)
