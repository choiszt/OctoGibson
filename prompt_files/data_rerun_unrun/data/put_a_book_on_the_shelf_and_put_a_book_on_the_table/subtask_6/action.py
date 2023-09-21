import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Move the robot to the table
    table = registry(env, "coffee_table_qlmqyy_0")
    MoveBot(env, robot, table, camera)
    donothing(env)
