import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Open the cabinet
    bottom_cabinet_jrhgeu_0 = registry(env,"bottom_cabinet_jrhgeu_0")
    open(robot, bottom_cabinet_jrhgeu_0)
    donothing(env)
