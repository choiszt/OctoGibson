import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the avocado from the shopping cart.
    avocado = registry(env, "avocado_142")
    EasyGrasp(robot, avocado)
    donothing(env)
