import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Grasp the steak
    steak = registry(env, "steak_172")
    EasyGrasp(robot, steak)
    donothing(env)
