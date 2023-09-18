import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the half apple pie inside the tupperware
    half_apple_pie_189 = registry(env,"half_apple_pie_189")
    tupperware_193 = registry(env,"tupperware_193")
    put_inside(robot, half_apple_pie_189, tupperware_193)
    donothing(env)
