import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Take out the salmon from the fridge
    salmon = registry(env, "salmon_85")
    EasyGrasp(robot, salmon)
    donothing(env)
