import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 9: Put the lamb on the platter.
    lamb = registry(env, "lamb_88")
    platter = registry(env, "platter_92")
    put_ontop(robot, lamb, platter)
    donothing(env)
