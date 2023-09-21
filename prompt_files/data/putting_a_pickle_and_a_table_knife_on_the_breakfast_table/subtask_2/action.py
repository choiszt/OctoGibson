import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the table knife from the bottom cabinet
    table_knife = registry(env, "table_knife_93")
    EasyGrasp(robot, table_knife)
    donothing(env)
