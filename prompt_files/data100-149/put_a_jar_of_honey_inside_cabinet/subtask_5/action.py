import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Move the robot to the front of the cabinet again
    bottom_cabinet_no_top_vzzafs_0 = registry(env,"bottom_cabinet_no_top_vzzafs_0")
    MoveBot(env, robot, bottom_cabinet_no_top_vzzafs_0, camera)
    donothing(env)
