import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Move to the table
    breakfast_table_skczfi_5 = registry(env,"breakfast_table_skczfi_5")
    MoveBot(env, robot, breakfast_table_skczfi_5, camera)
    donothing(env)
