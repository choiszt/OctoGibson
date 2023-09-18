import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the fax machine on the table
    facsimile_188 = registry(env,"facsimile_188")
    breakfast_table_skczfi_5 = registry(env,"breakfast_table_skczfi_5")
    put_ontop(robot, facsimile_188, breakfast_table_skczfi_5)
    donothing(env)
