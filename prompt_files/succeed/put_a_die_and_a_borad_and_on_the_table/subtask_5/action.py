import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the die on the table.
    dice_102 = registry(env,"dice_102")
    breakfast_table_dnsjnv_0 = registry(env,"breakfast_table_dnsjnv_0")
    put_ontop(robot, dice_102, breakfast_table_dnsjnv_0)
    donothing(env)
