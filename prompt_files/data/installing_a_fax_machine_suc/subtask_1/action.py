import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the fax machine
    facsimile_188 = registry(env,"facsimile_188")
    MoveBot(env, robot, facsimile_188, camera)
    donothing(env)
