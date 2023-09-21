import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the steak from the bottom cabinet
    steak = registry(env, "steak_172")
    EasyGrasp(robot, steak)
    donothing(env)
