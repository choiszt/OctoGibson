import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(env, robot, camera):
    fridge = registry("fridge_xyejdx_0")
    open(fridge)
    donothing(env)
