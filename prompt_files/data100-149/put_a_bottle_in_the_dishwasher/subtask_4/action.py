import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the bottle in the dishwasher
    dishwasher = registry(env, "dishwasher_dngvvi_0")
    baby_bottle = registry(env, "baby_bottle_85")
    put_inside(robot, baby_bottle, dishwasher)
    donothing(env)
