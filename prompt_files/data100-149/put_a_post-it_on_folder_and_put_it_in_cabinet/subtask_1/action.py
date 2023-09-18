import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Open the cabinet
    cabinet = registry(env, "bottom_cabinet_nddvba_0")
    open(robot, cabinet)
    donothing(env)
