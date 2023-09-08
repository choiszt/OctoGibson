import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Place the hot dogs on the frying pan
    hotdog_87 = registry(env, "hotdog_87")
    hotdog_86 = registry(env, "hotdog_86")
    frying_pan_85 = registry(env, "frying_pan_85")
    put_ontop(robot, hotdog_87, frying_pan_85)
    donothing(env)
    put_ontop(robot, hotdog_86, frying_pan_85)
    donothing(env)
