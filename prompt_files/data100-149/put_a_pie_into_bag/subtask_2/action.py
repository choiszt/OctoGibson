import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Grasp the hamburger_276
    hamburger_276 = registry(env,"hamburger_276")
    EasyGrasp(robot, hamburger_276)
    donothing(env)
