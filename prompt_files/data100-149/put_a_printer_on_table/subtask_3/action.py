import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the printer on the table
    printer_188 = registry(env,"printer_188")
    breakfast_table_skczfi_5 = registry(env,"breakfast_table_skczfi_5")
    put_ontop(robot, printer_188, breakfast_table_skczfi_5)
    donothing(env)
