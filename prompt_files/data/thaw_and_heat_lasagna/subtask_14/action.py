import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Put the lasagna inside the fridge
    lasagna_85 = registry(env,"lasagna_85")
    put_inside(robot, lasagna_85, fridge_xyejdx_0)
    donothing(env)
