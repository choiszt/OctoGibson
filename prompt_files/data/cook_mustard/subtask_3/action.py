import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move the robot to the bottom cabinet
    bottom_cabinet_no_top_qohxjq_0 = registry(env,"bottom_cabinet_no_top_qohxjq_0")
    MoveBot(env, robot, bottom_cabinet_no_top_qohxjq_0, camera)
    donothing(env)
