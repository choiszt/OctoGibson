import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the croissant
    croissant_283 = registry(env,"croissant_283")
    EasyGrasp(robot, croissant_283)
    donothing(env)
