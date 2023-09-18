import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the vase
    vase = registry(env, "vase_88")
    MoveBot(env, robot, vase, camera)
    donothing(env)
