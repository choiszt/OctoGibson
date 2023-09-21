import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the pickle on the breakfast table
    pickle = registry(env, "pickle_88")
    breakfast_table = registry(env, "breakfast_table_idnnmz_0")
    put_ontop(robot, pickle, breakfast_table)
    donothing(env)
