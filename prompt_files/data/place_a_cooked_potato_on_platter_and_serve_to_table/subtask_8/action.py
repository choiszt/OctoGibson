import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 8: Put the cooked potato on the platter
    potato = registry(env,"potato_89")
    platter = registry(env,"platter_92")
    put_ontop(robot, potato, platter)
    donothing(env)
