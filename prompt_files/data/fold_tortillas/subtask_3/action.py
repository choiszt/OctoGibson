import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the tortilla
    tortilla_153 = registry(env,"tortilla_153")
    EasyGrasp(robot, tortilla_153)
    donothing(env)
