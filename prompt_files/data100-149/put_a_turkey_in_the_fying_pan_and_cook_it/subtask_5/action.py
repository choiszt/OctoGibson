import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the turkey in the frying pan
    turkey_85 = registry(env,"turkey_85")
    frying_pan_88 = registry(env,"frying_pan_88")
    put_ontop(robot, turkey_85, frying_pan_88)
    donothing(env)
