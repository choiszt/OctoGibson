import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Heat the salmon on the countertop
    salmon = registry(env, "salmon_85")
    heat(robot, salmon)
    donothing(env)
