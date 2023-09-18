import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the hamburger from the fridge.
    hamburger = registry(env, "hamburger_85")
    EasyGrasp(robot, hamburger)
    donothing(env)
