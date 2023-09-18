import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move to the front of the cabinet
    cabinet = registry(env, "top_cabinet_dmwxyl_2")
    MoveBot(env, robot, cabinet, camera)
