import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 1: Open the cabinet
    bottom_cabinet_nddvba_0 = registry(env,"bottom_cabinet_nddvba_0")
    open(robot, bottom_cabinet_nddvba_0)
    donothing(env)
