import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 7: Cook the bowl with the apple inside
    bowl_88 = registry(env,"bowl_88")
    cook(robot, bowl_88)
    donothing(env)
