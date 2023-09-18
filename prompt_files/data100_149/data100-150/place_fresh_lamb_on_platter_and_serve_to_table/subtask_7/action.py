import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the platter from the bottom cabinet.
    platter = registry(env, "platter_92")
    EasyGrasp(robot, platter)
    donothing(env)
