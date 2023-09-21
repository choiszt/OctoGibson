import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the lasagna in the oven
    lasagna = registry(env,"lasagna_85")
    oven = registry(env,"oven_wuinhm_0")
    put_inside(robot, lasagna, oven)
    donothing(env)
