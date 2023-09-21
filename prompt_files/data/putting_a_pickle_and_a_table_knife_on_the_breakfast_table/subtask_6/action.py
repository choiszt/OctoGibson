import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the table knife on the breakfast table
    table_knife = registry(env, "table_knife_93")
    breakfast_table = registry(env, "breakfast_table_idnnmz_0")
    put_ontop(robot, table_knife, breakfast_table)
    donothing(env)
