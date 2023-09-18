import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Grasp the lamb from the fridge.
    lamb = registry(env, "lamb_88")
    EasyGrasp(robot, lamb)
    donothing(env)
