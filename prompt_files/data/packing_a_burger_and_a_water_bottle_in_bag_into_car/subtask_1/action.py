import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Grasp the hamburger
    hamburger_276 = registry(env,"hamburger_276")
    EasyGrasp(robot, hamburger_276)
    donothing(env)
