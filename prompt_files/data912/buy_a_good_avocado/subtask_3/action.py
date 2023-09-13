import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the avocado from the shopping cart
    avocado_142 = registry(env,"avocado_142")
    EasyGrasp(robot, avocado_142)
    donothing(env)
