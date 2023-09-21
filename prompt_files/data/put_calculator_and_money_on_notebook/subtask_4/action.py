import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the calculator on the notebook
    calculator_145 = registry(env,"calculator_145")
    notebook_148 = registry(env,"notebook_148")
    put_ontop(robot, calculator_145, notebook_148)
    donothing(env)
