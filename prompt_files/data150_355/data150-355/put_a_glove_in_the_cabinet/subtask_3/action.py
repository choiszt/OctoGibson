import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the cabinet
    top_cabinet_dmwxyl_3 = registry(env,"top_cabinet_dmwxyl_3")
    MoveBot(env, robot, top_cabinet_dmwxyl_3, camera)
    donothing(env)
