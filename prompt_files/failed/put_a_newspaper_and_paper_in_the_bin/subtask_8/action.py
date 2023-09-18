import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the notepad in the bin
    notepad_172 = registry(env,"notepad_172")
    recycling_bin_170 = registry(env,"recycling_bin_170")
    put_inside(robot, notepad_172, recycling_bin_170)
    donothing(env)
