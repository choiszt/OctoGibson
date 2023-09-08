import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Take out the hot dogs from the fridge
    hotdog_87 = registry(env, "hotdog_87")
    hotdog_86 = registry(env, "hotdog_86")
    EasyGrasp(robot, hotdog_87)
    donothing(env)
    EasyGrasp(robot, hotdog_86)
    donothing(env)
