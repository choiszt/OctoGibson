import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the die on the table
    die = registry(env, "dice_102")
    table = registry(env, "breakfast_table_dnsjnv_0")
    put_ontop(robot, die, table)
    donothing(env)
