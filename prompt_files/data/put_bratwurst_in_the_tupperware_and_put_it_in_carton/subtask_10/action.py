import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the tupperware from the bottom cabinet.
    tupperware = registry(env,"bottom_cabinet_no_top_spojpj_0")
    EasyGrasp(robot, tupperware)
    donothing(env)
