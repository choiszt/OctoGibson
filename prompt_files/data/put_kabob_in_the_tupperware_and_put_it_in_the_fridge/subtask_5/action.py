import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the kabob in the tupperware
    kabob_85 = registry(env,"kabob_85")
    tupperware_91 = registry(env,"tupperware_91")
    put_inside(robot, kabob_85, tupperware_91)
    donothing(env)
