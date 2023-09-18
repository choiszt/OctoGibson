import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the baking sheet
    baking_sheet_189 = registry(env,"baking_sheet_189")
    MoveBot(env, robot, baking_sheet_189, camera)
    donothing(env)
