import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move to the plate
    plate = registry(env,"plate_215")
    MoveBot(env, robot, plate, camera)
    donothing(env)
