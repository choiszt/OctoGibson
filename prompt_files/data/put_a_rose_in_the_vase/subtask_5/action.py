import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 3: Put the rose in the vase
    rose = registry(env, "rose_89")
    vase = registry(env, "vase_88")
    put_inside(robot, rose, vase)
    donothing(env)
