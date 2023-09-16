import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Cook the steak on the stove
    steak = registry(env,"steak_201")
    cook(robot, steak)
    donothing(env)
