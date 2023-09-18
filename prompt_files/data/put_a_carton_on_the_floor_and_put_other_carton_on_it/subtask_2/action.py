import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp carton_88
    carton_88 = registry(env, "carton_88")
    EasyGrasp(robot, carton_88)
    donothing(env)
