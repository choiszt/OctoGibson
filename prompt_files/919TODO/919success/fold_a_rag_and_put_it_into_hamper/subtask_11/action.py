import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the hamper
    hamper = registry(env, "hamper_188")
    MoveBot(env, robot, hamper, camera)
    donothing(env)
