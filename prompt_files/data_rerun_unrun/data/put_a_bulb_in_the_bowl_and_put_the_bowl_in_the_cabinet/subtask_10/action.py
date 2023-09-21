import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the top cabinet
    top_cabinet_dmwxyl_2 = registry(env,"top_cabinet_dmwxyl_2")
    MoveBot(env, robot, top_cabinet_dmwxyl_2, camera)
    donothing(env)
