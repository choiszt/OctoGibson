import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the teaspoon
    teaspoon = registry(env, "teaspoon")
    EasyGrasp(robot, teaspoon)
    donothing(env)
