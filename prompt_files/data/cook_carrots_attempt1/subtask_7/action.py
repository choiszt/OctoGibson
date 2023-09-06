import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the carrot.
    carrot = registry(env,"carrot_151")
    MoveBot(env, robot, carrot, camera)
    donothing(env)
