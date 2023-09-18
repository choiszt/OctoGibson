import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the spinach inside the compost bin
    spinach_189 = registry(env, "spinach_189")
    compost_bin_192 = registry(env, "compost_bin_192")
    put_inside(robot, spinach_189, compost_bin_192)
    donothing(env)
