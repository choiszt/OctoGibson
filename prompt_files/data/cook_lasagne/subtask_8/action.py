import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the lasagna inside the oven
    lasagna_85 = registry(env,"lasagna_85")
    oven_wuinhm_0 = registry(env,"oven_wuinhm_0")
    put_inside(robot, lasagna_85, oven_wuinhm_0)
    donothing(env)
