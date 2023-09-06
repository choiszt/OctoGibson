import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the saucepot object.
    saucepot = registry(env,"saucepot_150")
    # Subtask 2: Put the carrot into the saucepot.
    put_inside(robot, "carrot_151", saucepot)
    donothing(env)
