import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the notebook from the grocery_shelf_prtqlw_1
    notebook_148 = registry(env, "notebook_148")
    EasyGrasp(robot, notebook_148)
    donothing(env)
