import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the bottom cabinet
    bottom_cabinet_slgzfc_2 = registry(env,"bottom_cabinet_slgzfc_2")
    MoveBot(env, robot, bottom_cabinet_slgzfc_2, camera)
    donothing(env)
