import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Put the bread slice in the toaster
    bread_slice_87 = registry(env,"bread_slice_87")
    toaster_85 = registry(env,"toaster_85")
    put_inside(robot, bread_slice_87, toaster_85)
    donothing(env)
