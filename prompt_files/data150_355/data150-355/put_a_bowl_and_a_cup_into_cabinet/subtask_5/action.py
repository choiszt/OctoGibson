import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 5: Put the bowl inside the cabinet.
    bowl = registry(env, "bowl_190")
    cabinet = registry(env, "bottom_cabinet_no_top_ufhpbn_0")
    put_inside(robot, bowl, cabinet)
    donothing(env)
