import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the plate with the meatball
    plate_191 = registry(env,"plate_191")
    MoveBot(env, robot, plate_191, camera)
    donothing(env)
