import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Move the robot to the pencil
    colored_pencil_277 = registry(env,"colored_pencil_277")
    MoveBot(env, robot, colored_pencil_277, camera)
    donothing(env)
