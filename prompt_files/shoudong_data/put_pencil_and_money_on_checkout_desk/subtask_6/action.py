import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the colored_pencil_147 from the grocery_shelf_prtqlw_0
    colored_pencil_147 = registry(env, "colored_pencil_147")
    EasyGrasp(robot, colored_pencil_147)
    donothing(env)
