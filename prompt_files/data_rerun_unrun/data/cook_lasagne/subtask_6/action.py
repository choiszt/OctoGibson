import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the lasagna
    lasagna = registry(env, "lasagna_85")
    cook(robot, lasagna)
    donothing(env)
