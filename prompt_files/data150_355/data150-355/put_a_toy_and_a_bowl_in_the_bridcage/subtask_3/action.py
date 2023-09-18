import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the birdcage_188
    birdcage_188 = registry(env,"birdcage_188")
    MoveBot(env, robot, birdcage_188, camera)
    donothing(env)
