import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the fax machine and the table
    facsimile_188 = registry(env,"facsimile_188")
    breakfast_table_skczfi_5 = registry(env,"breakfast_table_skczfi_5")
    # Subtask 2: Toggle on the fax machine
    toggle_on(robot, facsimile_188)
    donothing(env)
