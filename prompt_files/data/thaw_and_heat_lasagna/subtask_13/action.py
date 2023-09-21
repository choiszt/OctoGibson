import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the lasagna in the fridge
    lasagna = registry(env,"lasagna_85")
    fridge = registry(env,"fridge_xyejdx_0")
    put_inside(robot, lasagna, fridge)
    donothing(env)
