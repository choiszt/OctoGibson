import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the saucer
    saucer_192 = registry(env,"saucer_192")
    MoveBot(env, robot, saucer_192, camera)
    donothing(env)
