import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move back to the cabinet
    cabinet = registry(env, "bottom_cabinet_nyfebf_0")
    MoveBot(env, robot, cabinet, camera)
    donothing(env)
