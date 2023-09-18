import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 4: Open the cabinet
    cabinet = registry(env, "bottom_cabinet_jrhgeu_0")
    open(robot, cabinet)
    donothing(env)
