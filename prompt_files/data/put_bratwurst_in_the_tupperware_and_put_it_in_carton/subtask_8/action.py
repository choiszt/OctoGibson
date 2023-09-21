import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 2: Open the bottom cabinet
    # We need to register the bottom cabinet first before we can interact with it.
    bottom_cabinet = registry(env, "bottom_cabinet_no_top_vzzafs_0")
    open(robot, bottom_cabinet)
    donothing(env)
