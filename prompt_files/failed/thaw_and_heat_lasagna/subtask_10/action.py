import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Register the lasagna
    lasagna_85 = registry(env,"lasagna_85")
    # Subtask 7: Put the lasagna inside the fridge
    put_inside(robot, lasagna_85, fridge_xyejdx_0)
    donothing(env)
