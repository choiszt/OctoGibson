import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the asparagus and green bean on the stove
    asparagus = registry(env, "asparagus_201")
    green_bean = registry(env, "green_bean_212")
    cook(robot, asparagus)
    donothing(env)
    cook(robot, green_bean)
    donothing(env)
