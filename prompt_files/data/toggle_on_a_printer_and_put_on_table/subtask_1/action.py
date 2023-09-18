import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the printer and the table
    printer = registry(env, "printer_188")
    table = registry(env, "breakfast_table_skczfi_5")
    
    # Subtask 2: Toggle on the printer
    toggle_on(robot, printer)
    donothing(env)
