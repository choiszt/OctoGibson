import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take the fish out of the fridge
    salmon = registry(env, "salmon_172")
    EasyGrasp(robot, salmon)
    donothing(env)
