import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 6: Close the cabinet
    cabinet = registry(env, "bottom_cabinet_jrhgeu_0")
    close(robot, cabinet)
    donothing(env)
