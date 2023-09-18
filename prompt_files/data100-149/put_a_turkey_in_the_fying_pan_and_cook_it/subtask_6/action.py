import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the turkey
    turkey_85 = registry(env,"turkey_85")
    cook(robot, turkey_85)
    donothing(env)
