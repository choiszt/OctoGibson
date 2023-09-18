import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Find a pan and put the brisket on it
    pan = registry(env,"pan_123") # Assume there is a pan in the environment
    brisket = registry(env,"brisket_189")
    put_ontop(robot, brisket, pan)
    donothing(env)
