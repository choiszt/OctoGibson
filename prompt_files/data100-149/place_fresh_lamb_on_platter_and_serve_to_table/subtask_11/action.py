import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 11: Put the platter with the lamb on the breakfast table.
    platter = registry(env, "platter_92")
    breakfast_table = registry(env, "breakfast_table_idnnmz_0")
    put_ontop(robot, platter, breakfast_table)
    donothing(env)
