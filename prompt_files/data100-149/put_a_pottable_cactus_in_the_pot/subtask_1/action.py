import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the pottable cactus
    pottable_cactus_275 = registry(env,"pottable_cactus_275")
    MoveBot(env, robot, pottable_cactus_275, camera)
    donothing(env)
