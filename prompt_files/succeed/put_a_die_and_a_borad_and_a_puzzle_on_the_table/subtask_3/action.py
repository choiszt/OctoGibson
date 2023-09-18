import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Move to the table
    table = registry(env, "breakfast_table_dnsjnv_0")
    MoveBot(env, robot, table, camera)
    donothing(env)
