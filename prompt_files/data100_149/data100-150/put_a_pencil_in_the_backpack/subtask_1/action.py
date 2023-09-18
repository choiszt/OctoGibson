import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the colored pencil
    colored_pencil_83 = registry(env,"colored_pencil_83")
    EasyGrasp(robot, colored_pencil_83)
    donothing(env)
