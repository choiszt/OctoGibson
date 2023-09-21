import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot, env, camera):
    # Subtask 4: Cook the carrot
    saucepot = registry(env, "saucepot_150")
    cook(robot, saucepot)
    donothing(env)
