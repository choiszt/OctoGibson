import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Turn on the fax machine
    facsimile_188 = registry(env,"facsimile_188")
    toggle_on(robot, facsimile_188)
    donothing(env)
