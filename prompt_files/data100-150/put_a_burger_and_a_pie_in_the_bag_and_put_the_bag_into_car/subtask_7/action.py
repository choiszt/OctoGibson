import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Find the croissant
    croissant_282 = registry(env,"croissant_282")
    # Subtask 7: Move the robot to the croissant
    MoveBot(env, robot, croissant_282, camera)
    donothing(env)
