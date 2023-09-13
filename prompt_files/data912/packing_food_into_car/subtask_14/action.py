import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Move the robot to the breakfast table
    breakfast_table = registry(env, "breakfast_table_ytelxk_0")
    MoveBot(env, robot, breakfast_table, camera)
    donothing(env)
