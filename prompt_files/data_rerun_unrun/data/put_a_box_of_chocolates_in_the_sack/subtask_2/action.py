import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the box of chocolates
    box_of_chocolates = registry(env, "box_of_chocolates_91")
    EasyGrasp(robot, box_of_chocolates)
    donothing(env)
