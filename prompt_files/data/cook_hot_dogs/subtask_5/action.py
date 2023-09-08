import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Cook the hot dogs
    hotdog_87 = registry(env, "hotdog_87")
    hotdog_86 = registry(env, "hotdog_86")
    cook(robot, hotdog_87)
    donothing(env)
    cook(robot, hotdog_86)
    donothing(env)
