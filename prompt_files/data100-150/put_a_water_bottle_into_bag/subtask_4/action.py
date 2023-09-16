import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Open the suitcase
    suitcase = registry(env, "suitcase_285")
    open(robot, suitcase)
    donothing(env)
