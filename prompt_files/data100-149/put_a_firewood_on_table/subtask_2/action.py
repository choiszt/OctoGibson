import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the firewood
    firewood_275 = registry(env,"firewood_275")
    EasyGrasp(robot, firewood_275)
    donothing(env)
