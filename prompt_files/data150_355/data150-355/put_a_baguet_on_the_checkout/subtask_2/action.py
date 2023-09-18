import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the baguette
    baguette = registry(env, "baguette_143")
    EasyGrasp(robot, baguette)
    donothing(env)
