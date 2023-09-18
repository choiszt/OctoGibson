import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the bread slice in the toaster
    toaster = registry(env, "toaster_85")
    bread_slice = registry(env, "bread_slice_87")
    put_ontop(robot, bread_slice, toaster)
    donothing(env)
