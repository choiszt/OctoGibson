import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Take the prawn from the plate
    shrimp = registry(env,"shrimp_201")
    EasyGrasp(robot, shrimp)
    donothing(env)
