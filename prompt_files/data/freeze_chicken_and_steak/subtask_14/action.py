import os 
import json
import yaml
import omnigibson as og
from action_list import * 
from action_utils import *
def act(robot,env,camera):
    # Subtask 11: Freeze the chicken
    chicken = registry(env, "chicken_176")
    freeze(robot, chicken)
    donothing(env)
