import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Register the dishwasher and the bottle
    dishwasher = registry(env, "dishwasher_dngvvi_0")
    bottle = registry(env, "baby_bottle_85")
    # Subtask 2: Grasp the bottle
    EasyGrasp(robot, bottle)
    donothing(env)
